import type { NextApiRequest, NextApiResponse } from 'next';
import path from 'path';
import fs from 'fs';

const NFTS = path.join(process.cwd(),'data','nfts.json');

export default function handler(req: NextApiRequest, res: NextApiResponse){
  const raw = fs.readFileSync(NFTS,'utf8');
  const nfts = JSON.parse(raw);
  res.status(200).json(nfts);
}