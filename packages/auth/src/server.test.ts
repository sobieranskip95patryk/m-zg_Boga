import request from 'supertest';
import express from 'express';
import { Server } from 'http';

const app = express();
app.use(express.json());
app.post('/register', (req, res) => res.json({ success: true }));
app.post('/login', (req, res) => res.json({ token: 'mocktoken' }));
let server: Server;

beforeAll(() => {
  server = app.listen(4001);
});
afterAll(() => {
  server.close();
});

test('POST /register returns success', async () => {
  const res = await request(app)
    .post('/register')
    .send({ username: 'admin', password: 'pass123', role: 'admin' });
  expect(res.body.success).toBe(true);
});

test('POST /login returns token', async () => {
  const res = await request(app)
    .post('/login')
    .send({ username: 'admin', password: 'pass123' });
  expect(res.body.token).toBe('mocktoken');
});
