import express from 'express';
import jwt from 'jsonwebtoken';
import axios from 'axios';

const app = express();
app.use(express.json());

// Middleware do walidacji JWT i roli
app.use((req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token provided' });
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET || 'supersecret') as { role: string };
    if (decoded.role !== 'admin' && decoded.role !== 'agent') {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    next();
  } catch (e) {
    res.status(403).json({ error: 'Invalid token' });
  }
});

// Przykład endpointu do analizy (np. geo/security z AnonymousAgent)
app.post('/analyze', async (req, res) => {
  const { data } = req.body;
  // Mock analizy (zastąp logiką z AnonymousAgent_2.0, np. geo IP scan)
  try {
    // Przykład integracji z xAI/Grok przez orchestrator
    const grokResponse = await axios.post('http://localhost:3000/route', {
      type: 'ai-avatar',
      data: { query: `Analyze security data: ${JSON.stringify(data)}` },
    }, {
      headers: { Authorization: req.headers.authorization }
    });
    res.json({
      result: 'Security analysis complete',
      grokInsights: grokResponse.data,
    });
  } catch (e) {
    res.status(500).json({ error: 'Analysis failed' });
  }
});

app.listen(3002, () => console.log('AnonymousAgent running on port 3002'));
