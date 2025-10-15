import request from 'supertest';
import express from 'express';
import { Server } from 'http';
import jwt from 'jsonwebtoken';

const app = express();
app.use(express.json());
app.post('/analyze', (req, res) => res.json({ result: 'Security analysis complete' }));
let server: Server;

beforeAll(() => {
  server = app.listen(4002);
});
afterAll(() => {
  server.close();
});

test('POST /analyze returns result', async () => {
  const token = jwt.sign({ role: 'admin' }, 'supersecret');
  const res = await request(app)
    .post('/analyze')
    .set('Authorization', `Bearer ${token}`)
    .send({ data: {} });
  expect(res.body.result).toBe('Security analysis complete');
});
