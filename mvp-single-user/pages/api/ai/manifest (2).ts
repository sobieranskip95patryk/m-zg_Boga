import type { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if(req.method !== 'POST') return res.status(405).end();
  const body = req.body ? req.body : JSON.parse(req.body);
  const prompt = String(body.prompt || '');
  // PROSTY RULE-BASED "AI" — placeholder dla GPT-4 integ.
  const manifest = [
    "1) Cel: Tworzyć technologie które podnoszą świadomość.",
    "2) Metoda: Integracja AI + blockchain + kultura.",
    "3) Imperatyw: Transparentność, decentralizacja, etyka.",
    "4) Akcja: Publikuj, współpracuj, tokenizuj wartościowe artefakty."
  ];
  res.status(200).json({ manifest: manifest.join('\n') });
}