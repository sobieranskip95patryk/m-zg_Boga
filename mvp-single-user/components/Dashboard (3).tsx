import useSWR from 'swr';
import { useState } from 'react';
const fetcher = (u: string) => fetch(u).then(r => r.json());

export default function Dashboard(){
  const { data: nfts } = useSWR('/api/nfts', fetcher);
  const [price, setPrice] = useState(100);
  const [title, setTitle] = useState('Consciousness Token #');

  async function mint(){
    const res = await fetch('/api/mint', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ price, title })
    });
    const j = await res.json();
    if(j.success) {
      alert('Zmintowano NFT: id=' + j.nft.id);
      location.reload();
    } else {
      alert('Błąd: ' + j.error);
    }
  }

  return (
    <div>
      <h4>Creator quick actions</h4>
      <div style={{marginBottom:8}}>
        <input value={title} onChange={e=>setTitle(e.target.value)} style={{width:'100%'}}/>
      </div>
      <div style={{display:'flex', gap:8}}>
        <input type="number" value={price} onChange={e=>setPrice(Number(e.target.value))} />
        <button onClick={mint}>Mint NFT ({price} DRT)</button>
      </div>

      <hr />
      <h4>Twoje NFT</h4>
      {!nfts ? <div>Ładowanie…</div> :
        nfts.length === 0 ? <div>Brak NFT</div> :
        nfts.map((n:any)=>(
          <div key={n.id} className="nft-card">
            <strong>{n.title}</strong>
            <div>ID: {n.id}</div>
            <div>Owner: {n.owner}</div>
            <div>Price: {n.price} DRT</div>
            <small>Minted at: {new Date(n.mintedAt).toLocaleString()}</small>
          </div>
        ))
      }
    </div>
  )
}