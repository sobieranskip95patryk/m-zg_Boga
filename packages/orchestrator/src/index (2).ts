import express from 'express';
import jwt from 'jsonwebtoken';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(express.json());

// Middleware do walidacji JWT
app.use((req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token provided' });
  try {
    jwt.verify(token, process.env.JWT_SECRET || 'supersecret');
    next();
  } catch (e) {
    res.status(403).json({ error: 'Invalid token' });
  }
});

// Route do routingu requestów do agentów
app.post('/route', async (req, res) => {
  const { type, data } = req.body;
  let targetUrl = '';
  switch (type) {
    case 'security': targetUrl = 'http://anonymous-agent:3002/analyze'; break;
    case 'ai-avatar': targetUrl = 'http://pinkman:3003/process'; break;
    default: return res.status(400).json({ error: 'Unknown agent type' });
  }
  try {
    const response = await axios.post(targetUrl, data, {
      headers: { Authorization: req.headers.authorization }
    });
    res.json(response.data);
  } catch (e) {
    res.status(500).json({ error: 'Agent communication failed' });
  }
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

app.listen(3000, () => console.log('Orchestrator running on port 3000'));
