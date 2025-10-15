import type { NextApiRequest, NextApiResponse } from 'next';
import path from 'path';
import fs from 'fs';

const STATE = path.join(process.cwd(),'data','state.json');
const NFTS = path.join(process.cwd(),'data','nfts.json');

export default function handler(req: NextApiRequest, res: NextApiResponse){
  if(req.method !== 'POST') return res.status(405).end();
  const body = req.body ? req.body : JSON.parse(req.body);
  const price = Number(body.price || 0);
  const title = String(body.title || `Consciousness #${Date.now()}`);

  const rawState = fs.readFileSync(STATE,'utf8');
  const state = JSON.parse(rawState);

  if(state.drtBalance < price) {
    return res.status(400).json({ success:false, error: 'Insufficient DRT balance' });
  }

  // deduct
  state.drtBalance -= price;
  const nftRaw = fs.readFileSync(NFTS,'utf8');
  const nfts = JSON.parse(nftRaw);

  const nft = {
    id: state.nextNftId,
    title,
    price,
    owner: 'patryk-sobieranski',
    mintedAt: new Date().toISOString(),
    metadataUri: `ipfs://mock/${state.nextNftId}`
  };
  nfts.push(nft);
  state.nextNftId += 1;

  fs.writeFileSync(NFTS, JSON.stringify(nfts, null, 2));
  fs.writeFileSync(STATE, JSON.stringify(state, null, 2));

  res.status(200).json({ success: true, nft });
}