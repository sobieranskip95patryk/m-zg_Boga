import type { NextApiRequest, NextApiResponse } from 'next';
import path from 'path';
import fs from 'fs';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const file = path.join(process.cwd(), 'data', 'profiles', 'patryk_sobieranski.json');
  const raw = fs.readFileSync(file, 'utf8');
  res.status(200).json(JSON.parse(raw));
}