const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('AnonymousAgent 2.0 API działa!');
});

// Endpoint do analizy profilu
app.post('/analyze', async (req, res) => {
  // Tu podłącz logikę GeoScanner, IntentAnalyzer itd.
  res.json({ status: 'ok', result: 'analyzed' });
});

app.listen(port, () => {
  console.log(`Serwer działa na porcie ${port}`);
});
