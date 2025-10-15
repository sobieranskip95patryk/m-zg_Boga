const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL || 'postgresql://postgres:postgres@localhost:5432/hiphop',
  ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: false } : false
});

module.exports = {
  query: (text, params) => pool.query(text, params),
  pool,
  
  // Helper functions
  async testConnection() {
    try {
      const client = await pool.connect();
      const result = await client.query('SELECT NOW()');
      client.release();
      console.log('✅ Database connected:', result.rows[0].now);
      return true;
    } catch (err) {
      console.error('❌ Database connection error:', err.message);
      return false;
    }
  }
};