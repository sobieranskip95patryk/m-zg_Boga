require('dotenv').config();
const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const db = require('./db');

const app = express();

// Middleware
app.use(cors());
app.use(morgan('combined'));
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Routes
const mintRouter = require('./routes/mint');
const aiRouter = require('./routes/ai');

app.use('/api/mint', mintRouter);
app.use('/api/ai', aiRouter);

// Health check
app.get('/health', async (req, res) => {
  const dbOk = await db.testConnection();
  res.json({ 
    status: 'ok', 
    timestamp: new Date().toISOString(),
    database: dbOk ? 'connected' : 'disconnected',
    environment: process.env.NODE_ENV || 'development'
  });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({ 
    message: '🎵 Hip-Hop Universe API', 
    version: '1.0.0',
    endpoints: ['/api/mint', '/api/ai', '/health']
  });
});

const PORT = process.env.PORT || 4000;

app.listen(PORT, async () => {
  console.log(`🚀 Hip-Hop Universe Backend listening on port ${PORT}`);
  console.log(`🌐 Environment: ${process.env.NODE_ENV || 'development'}`);
  
  // Test database connection on startup
  await db.testConnection();
});