// server.js - Rocket Fuell Girls Backend
const express = require('express');
const multer = require('multer');
const sharp = require('sharp');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const sqlite3 = require('sqlite3').verbose();
const { open } = require('sqlite');
const cors = require('cors');

const app = express();

// Directories setup
const UP_DIR = path.join(__dirname, 'uploads');
const ORIG_DIR = path.join(UP_DIR, 'originals');
const TH_DIR = path.join(UP_DIR, 'thumbs');

// Create directories if they don't exist
for (const dir of [UP_DIR, ORIG_DIR, TH_DIR]) {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
}

// Multer configuration
const storage = multer.memoryStorage();
const upload = multer({
    storage,
    limits: { 
        fileSize: 8 * 1024 * 1024, // 8MB limit
        files: 5 // max 5 files per upload
    },
    fileFilter: (req, file, cb) => {
        const allowedTypes = /jpeg|jpg|png/;
        const mimeCheck = allowedTypes.test(file.mimetype);
        const extCheck = allowedTypes.test(path.extname(file.originalname).toLowerCase());
        
        if (mimeCheck && extCheck) {
            return cb(null, true);
        } else {
            cb(new Error('Tylko pliki JPEG, JPG i PNG są dozwolone!'));
        }
    }
});

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/uploads', express.static(UP_DIR));
app.use(express.static(path.join(__dirname)));

// Database initialization
let db;
(async () => {
    try {
        db = await open({ 
            filename: './rocket_fuell.db', 
            driver: sqlite3.Database 
        });
        
        // Create tables
        await db.exec(`
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            
            CREATE TABLE IF NOT EXISTS photos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                filename TEXT NOT NULL,
                thumb TEXT NOT NULL,
                original_name TEXT,
                caption TEXT,
                height INTEGER,
                location TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                approved INTEGER DEFAULT 0,
                views INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );
            
            CREATE TABLE IF NOT EXISTS admin_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        `);
        
        console.log('✅ Database initialized successfully');
    } catch (error) {
        console.error('❌ Database initialization failed:', error);
        process.exit(1);
    }
})();

// Utility functions
function generateRandomFilename(ext = 'jpg') {
    return crypto.randomBytes(16).toString('hex') + '.' + ext;
}

function sanitizeInput(input, maxLength = 300) {
    return String(input || '').trim().slice(0, maxLength)
        .replace(/<[^>]*>/g, '') // Remove HTML tags
        .replace(/[<>&"']/g, ''); // Remove potentially dangerous chars
}

// API Routes

// Upload endpoint
app.post('/api/upload', upload.array('photos', 5), async (req, res) => {
    try {
        if (!req.files || req.files.length === 0) {
            return res.status(400).json({ error: 'Nie przesłano żadnych plików' });
        }

        const { name, email, caption, height, location } = req.body;
        
        // Validate and sanitize inputs
        const userName = sanitizeInput(name, 100);
        const userEmail = sanitizeInput(email, 150);
        const userCaption = sanitizeInput(caption, 500);
        const userHeight = height ? parseInt(height) : null;
        const userLocation = sanitizeInput(location, 100);

        if (!userName) {
            return res.status(400).json({ error: 'Imię jest wymagane' });
        }

        // Create or get user
        let user = await db.get('SELECT id FROM users WHERE name = ? AND email = ?', userName, userEmail);
        if (!user) {
            const result = await db.run(
                'INSERT INTO users (name, email) VALUES (?, ?)', 
                userName, userEmail
            );
            user = { id: result.lastID };
        }

        const uploadedFiles = [];

        // Process each uploaded file
        for (const file of req.files) {
            const ext = file.mimetype === 'image/png' ? 'png' : 'jpg';
            const filename = generateRandomFilename(ext);
            const thumbName = generateRandomFilename('jpg');

            // Process original image (remove EXIF, optimize)
            const processedImage = sharp(file.buffer)
                .rotate() // Auto-rotate based on EXIF orientation
                .resize(2000, 2000, { 
                    fit: 'inside',
                    withoutEnlargement: true 
                });

            // Save original
            await processedImage
                .toFormat(ext === 'png' ? 'png' : 'jpeg', { 
                    quality: 88,
                    progressive: true 
                })
                .toFile(path.join(ORIG_DIR, filename));

            // Create thumbnail
            await sharp(file.buffer)
                .rotate()
                .resize(800, 1200, { 
                    fit: 'inside',
                    withoutEnlargement: true 
                })
                .jpeg({ 
                    quality: 82,
                    progressive: true 
                })
                .toFile(path.join(TH_DIR, thumbName));

            // Save to database
            await db.run(`
                INSERT INTO photos (user_id, filename, thumb, original_name, caption, height, location, approved) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            `, user.id, filename, thumbName, file.originalname, userCaption, userHeight, userLocation, 0);

            uploadedFiles.push({
                filename,
                thumb: thumbName,
                originalName: file.originalname
            });
        }

        res.json({ 
            success: true, 
            message: `Przesłano ${uploadedFiles.length} zdjęć. Oczekują na moderację.`,
            files: uploadedFiles
        });

    } catch (error) {
        console.error('Upload error:', error);
        res.status(500).json({ 
            error: error.message || 'Błąd podczas przesyłania plików' 
        });
    }
});

// Get approved photos for public gallery
app.get('/api/photos', async (req, res) => {
    try {
        const page = parseInt(req.query.page) || 1;
        const limit = parseInt(req.query.limit) || 20;
        const offset = (page - 1) * limit;

        const photos = await db.all(`
            SELECT 
                p.id, 
                p.caption, 
                p.thumb, 
                p.filename, 
                p.height,
                p.location,
                p.views,
                p.created_at,
                u.name AS author
            FROM photos p 
            LEFT JOIN users u ON p.user_id = u.id 
            WHERE p.approved = 1 
            ORDER BY p.created_at DESC 
            LIMIT ? OFFSET ?
        `, limit, offset);

        const totalCount = await db.get('SELECT COUNT(*) as count FROM photos WHERE approved = 1');

        const photosWithUrls = photos.map(photo => ({
            id: photo.id,
            caption: photo.caption,
            author: photo.author,
            height: photo.height,
            location: photo.location,
            views: photo.views,
            created_at: photo.created_at,
            url: `/uploads/originals/${photo.filename}`,
            thumb: `/uploads/thumbs/${photo.thumb}`
        }));

        res.json({
            photos: photosWithUrls,
            total: totalCount.count,
            page,
            totalPages: Math.ceil(totalCount.count / limit)
        });

    } catch (error) {
        console.error('Get photos error:', error);
        res.status(500).json({ error: 'Błąd podczas pobierania zdjęć' });
    }
});

// Get photo details and increment view count
app.get('/api/photo/:id', async (req, res) => {
    try {
        const photoId = parseInt(req.params.id);
        
        // Increment view count
        await db.run('UPDATE photos SET views = views + 1 WHERE id = ? AND approved = 1', photoId);
        
        // Get photo details
        const photo = await db.get(`
            SELECT 
                p.id, 
                p.caption, 
                p.thumb, 
                p.filename, 
                p.height,
                p.location,
                p.views,
                p.created_at,
                u.name AS author,
                u.email AS author_email
            FROM photos p 
            LEFT JOIN users u ON p.user_id = u.id 
            WHERE p.id = ? AND p.approved = 1
        `, photoId);

        if (!photo) {
            return res.status(404).json({ error: 'Zdjęcie nie zostało znalezione' });
        }

        res.json({
            id: photo.id,
            caption: photo.caption,
            author: photo.author,
            height: photo.height,
            location: photo.location,
            views: photo.views,
            created_at: photo.created_at,
            url: `/uploads/originals/${photo.filename}`,
            thumb: `/uploads/thumbs/${photo.thumb}`
        });

    } catch (error) {
        console.error('Get photo error:', error);
        res.status(500).json({ error: 'Błąd podczas pobierania zdjęcia' });
    }
});

// Admin endpoints (simplified - add proper auth in production!)
app.get('/api/admin/pending', async (req, res) => {
    try {
        const pendingPhotos = await db.all(`
            SELECT 
                p.id, 
                p.caption, 
                p.thumb, 
                p.filename, 
                p.height,
                p.location,
                p.created_at,
                u.name AS author,
                u.email AS author_email
            FROM photos p 
            LEFT JOIN users u ON p.user_id = u.id 
            WHERE p.approved = 0 
            ORDER BY p.created_at ASC
        `);

        const photosWithUrls = pendingPhotos.map(photo => ({
            id: photo.id,
            caption: photo.caption,
            author: photo.author,
            author_email: photo.author_email,
            height: photo.height,
            location: photo.location,
            created_at: photo.created_at,
            url: `/uploads/originals/${photo.filename}`,
            thumb: `/uploads/thumbs/${photo.thumb}`
        }));

        res.json(photosWithUrls);
    } catch (error) {
        console.error('Get pending photos error:', error);
        res.status(500).json({ error: 'Błąd podczas pobierania zdjęć do moderacji' });
    }
});

app.post('/api/admin/approve/:id', async (req, res) => {
    try {
        const photoId = parseInt(req.params.id);
        await db.run('UPDATE photos SET approved = 1 WHERE id = ?', photoId);
        res.json({ success: true, message: 'Zdjęcie zostało zatwierdzone' });
    } catch (error) {
        console.error('Approve photo error:', error);
        res.status(500).json({ error: 'Błąd podczas zatwierdzania zdjęcia' });
    }
});

app.delete('/api/admin/reject/:id', async (req, res) => {
    try {
        const photoId = parseInt(req.params.id);
        
        // Get file names before deletion
        const photo = await db.get('SELECT filename, thumb FROM photos WHERE id = ?', photoId);
        
        if (photo) {
            // Delete files from filesystem
            const originalPath = path.join(ORIG_DIR, photo.filename);
            const thumbPath = path.join(TH_DIR, photo.thumb);
            
            if (fs.existsSync(originalPath)) fs.unlinkSync(originalPath);
            if (fs.existsSync(thumbPath)) fs.unlinkSync(thumbPath);
        }
        
        // Delete from database
        await db.run('DELETE FROM photos WHERE id = ?', photoId);
        
        res.json({ success: true, message: 'Zdjęcie zostało odrzucone i usunięte' });
    } catch (error) {
        console.error('Reject photo error:', error);
        res.status(500).json({ error: 'Błąd podczas odrzucania zdjęcia' });
    }
});

// Admin panel route
app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'admin.html'));
});

// Health check
app.get('/api/health', (req, res) => {
    res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// Error handling middleware
app.use((error, req, res, next) => {
    console.error('Global error handler:', error);
    
    if (error instanceof multer.MulterError) {
        if (error.code === 'LIMIT_FILE_SIZE') {
            return res.status(400).json({ error: 'Plik jest za duży (max 8MB)' });
        }
        if (error.code === 'LIMIT_FILE_COUNT') {
            return res.status(400).json({ error: 'Za dużo plików (max 5)' });
        }
    }
    
    res.status(500).json({ 
        error: 'Wystąpił błąd serwera',
        details: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 Rocket Fuell Girls server running on port ${PORT}`);
    console.log(`📱 Frontend: http://localhost:${PORT}`);
    console.log(`🔧 Admin panel: http://localhost:${PORT}/admin`);
    console.log(`📊 Health check: http://localhost:${PORT}/api/health`);
});

module.exports = app;