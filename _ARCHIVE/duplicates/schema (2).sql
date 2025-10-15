-- Rocket Fuell Girls Database Schema
-- SQLite database structure for the photo gallery platform

-- Table for storing user information
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    bio TEXT,
    instagram TEXT,
    website TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing photo information
CREATE TABLE IF NOT EXISTS photos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    filename TEXT NOT NULL,           -- Original file name on server
    thumb TEXT NOT NULL,              -- Thumbnail file name
    original_name TEXT,               -- Original upload file name
    caption TEXT,                     -- Photo description
    height INTEGER,                   -- Model height in cm
    location TEXT,                    -- Shooting location
    tags TEXT,                        -- Comma-separated tags
    file_size INTEGER,                -- File size in bytes
    width INTEGER,                    -- Image width in pixels
    height_px INTEGER,                -- Image height in pixels
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    approved INTEGER DEFAULT 0,       -- 0 = pending, 1 = approved, -1 = rejected
    approved_at DATETIME,             -- When photo was approved
    approved_by INTEGER,              -- Admin user who approved
    views INTEGER DEFAULT 0,          -- Number of views
    likes INTEGER DEFAULT 0,          -- Number of likes
    featured INTEGER DEFAULT 0,       -- Featured photo flag
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (approved_by) REFERENCES admin_users (id)
);

-- Table for admin users
CREATE TABLE IF NOT EXISTS admin_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT,
    role TEXT DEFAULT 'moderator',   -- moderator, admin, super_admin
    last_login DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    active INTEGER DEFAULT 1
);

-- Table for photo likes (if implementing like system)
CREATE TABLE IF NOT EXISTS photo_likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    photo_id INTEGER,
    user_ip TEXT,                    -- For anonymous likes tracking
    user_agent TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (photo_id) REFERENCES photos (id),
    UNIQUE(photo_id, user_ip)        -- Prevent duplicate likes from same IP
);

-- Table for moderation log
CREATE TABLE IF NOT EXISTS moderation_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    photo_id INTEGER,
    admin_id INTEGER,
    action TEXT,                     -- 'approved', 'rejected', 'deleted'
    reason TEXT,                     -- Reason for rejection
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (photo_id) REFERENCES photos (id),
    FOREIGN KEY (admin_id) REFERENCES admin_users (id)
);

-- Table for system settings
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT,
    description TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_photos_approved ON photos(approved);
CREATE INDEX IF NOT EXISTS idx_photos_created_at ON photos(created_at);
CREATE INDEX IF NOT EXISTS idx_photos_user_id ON photos(user_id);
CREATE INDEX IF NOT EXISTS idx_photos_views ON photos(views);
CREATE INDEX IF NOT EXISTS idx_photo_likes_photo_id ON photo_likes(photo_id);
CREATE INDEX IF NOT EXISTS idx_photo_likes_ip ON photo_likes(user_ip);

-- Insert default settings
INSERT OR IGNORE INTO settings (key, value, description) VALUES 
('max_file_size', '8388608', 'Maximum file size in bytes (8MB)'),
('max_files_per_upload', '5', 'Maximum number of files per upload'),
('allowed_file_types', 'jpeg,jpg,png', 'Allowed file extensions'),
('auto_approve', '0', 'Auto-approve uploads (0=no, 1=yes)'),
('require_email', '1', 'Require email for uploads (0=no, 1=yes)'),
('site_title', 'Rocket Fuell Girls', 'Site title'),
('site_description', 'Platforma dla modelek do prezentacji portfolio', 'Site description');

-- Insert default admin user (password: admin123 - CHANGE IN PRODUCTION!)
-- Note: In production, hash this password properly!
INSERT OR IGNORE INTO admin_users (username, password_hash, email, role) VALUES 
('admin', '$2b$10$rXEgwBQhTKPxGLKe2pEyqeO9w0JtzEhBnmHJgF5hI4K4ZHE2a7lOy', 'admin@rocketfuellgirls.com', 'admin');