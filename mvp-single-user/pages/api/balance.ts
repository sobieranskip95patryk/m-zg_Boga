import type { NextApiRequest, NextApiResponse } from 'next';
import path from 'path';
import fs from 'fs';

const STATE = path.join(process.cwd(),'data','state.json');

export default function handler(req: NextApiRequest, res: NextApiResponse){
  const raw = fs.readFileSync(STATE,'utf8');
  const state = JSON.parse(raw);
  res.status(200).json({ drtBalance: state.drtBalance });
}