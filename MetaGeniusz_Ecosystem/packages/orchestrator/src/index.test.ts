import request from 'supertest';
import express from 'express';
import { Server } from 'http';
import jwt from 'jsonwebtoken';

const app = express();
app.use(express.json());
app.post('/route', (req, res) => res.json({ ok: true }));
let server: Server;

beforeAll(() => {
  server = app.listen(4000);
});
afterAll(() => {
  server.close();
});

test('POST /route returns ok', async () => {
  const token = jwt.sign({ role: 'admin' }, 'supersecret');
  const res = await request(app)
    .post('/route')
    .set('Authorization', `Bearer ${token}`)
    .send({ type: 'security', data: {} });
  expect(res.body.ok).toBe(true);
});
