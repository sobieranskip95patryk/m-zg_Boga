import useSWR from 'swr';
import ProfileCard from '../components/ProfileCard';
import Dashboard from '../components/Dashboard';

const fetcher = (u: string) => fetch(u).then(r => r.json());

export default function Home() {
  const { data: profile } = useSWR('/api/profile', fetcher);
  const { data: balance } = useSWR('/api/balance', fetcher);

  return (
    <div className="container">
      <h1>Hip-Hop Universe — MVP (single user)</h1>
      <div style={{marginTop:12}} className="row">
        <div className="col card">
          {profile ? <ProfileCard profile={profile} /> : <div>Ładowanie profilu…</div>}
        </div>
        <div style={{width:320}} className="card">
          <h3>Wallet / DRT</h3>
          <p><strong>DRT balance:</strong> {balance?.drtBalance ?? '…'}</p>
          <button onClick={async ()=> {
            await fetch('/api/topup', {method:'POST', body: JSON.stringify({amount:500}), headers:{'Content-Type':'application/json'}});
            location.reload();
          }}>Top-up +500 DRT</button>
          <hr />
          <Dashboard />
        </div>
      </div>
    </div>
  )
}