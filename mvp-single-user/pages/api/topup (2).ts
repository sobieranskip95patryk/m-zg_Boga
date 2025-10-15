import type { NextApiRequest, NextApiResponse } from 'next';
import path from 'path';
import fs from 'fs';

const STATE = path.join(process.cwd(),'data','state.json');

export default function handler(req: NextApiRequest, res: NextApiResponse){
  if (req.method !== 'POST') return res.status(405).end();
  const body = req.body ? req.body : JSON.parse(req.body);
  const amount = Number(body.amount || 0);
  if (isNaN(amount) || amount <= 0) return res.status(400).json({error:'invalid amount'});
  const raw = fs.readFileSync(STATE,'utf8');
  const state = JSON.parse(raw);
  state.drtBalance = (state.drtBalance || 0) + amount;
  fs.writeFileSync(STATE, JSON.stringify(state, null, 2));
  res.status(200).json({ success: true, drtBalance: state.drtBalance });
}