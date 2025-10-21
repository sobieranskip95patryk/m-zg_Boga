import express from 'express';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

const app = express();
app.use(express.json());

// Mock DB (zastąp MongoDB/Supabase w prod)
const users: { [key: string]: { hashed: string; role: string } } = {};

// Register endpoint
app.post('/register', async (req, res) => {
  const { username, password, role } = req.body;
  if (!['admin', 'user', 'agent'].includes(role)) {
    return res.status(400).json({ error: 'Invalid role' });
  }
  const hashed = await bcrypt.hash(password, 10);
  users[username] = { hashed, role };
  res.json({ success: true });
});

// Login endpoint -> JWT
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = users[username];
  if (!user || !(await bcrypt.compare(password, user.hashed))) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  const token = jwt.sign({ username, role: user.role }, process.env.JWT_SECRET || 'supersecret', { expiresIn: '1h' });
  res.json({ token });
});

app.listen(3001, () => console.log('Auth service running on port 3001'));
