const axios = require('axios');

// Przykład testu integracji z backendem
async function testAnalyze() {
  const profile = {
    id: 'user123',
    ip: '8.8.8.8',
    trustScore: 0.2,
    activity: 0,
    lastMessage: 'Send me bitcoin, urgent!'
  };
  const res = await axios.post('http://localhost:3000/analyze', profile);
  console.log('Wynik analizy:', res.data);
}

testAnalyze();
