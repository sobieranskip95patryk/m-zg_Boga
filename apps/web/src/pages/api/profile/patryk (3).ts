// pages/api/profile/patryk.ts
import type { NextApiRequest, NextApiResponse } from 'next';
import path from 'path';
import fs from 'fs';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'GET') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const filePath = path.join(process.cwd(), '../../data', 'profiles', 'patryk_sobieranski.json');
    const raw = fs.readFileSync(filePath, 'utf8');
    const profile = JSON.parse(raw);
    
    // Cache headers for better performance
    res.setHeader('Cache-Control', 'public, s-maxage=3600, stale-while-revalidate=86400');
    res.status(200).json(profile);
  } catch (error) {
    console.error('Error loading profile:', error);
    res.status(500).json({ error: 'Failed to load profile' });
  }
}