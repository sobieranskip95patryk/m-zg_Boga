import React from 'react';

export default function ProfileCard({ profile }: any) {
  return (
    <div>
      <div className="row" style={{alignItems:'center'}}>
        <div className="profile-avatar">
          {profile.displayName.split(' ').map((n:string)=>n[0]).slice(0,2).join('')}
        </div>
        <div style={{flex:1}}>
          <h2>{profile.displayName} <small> — {profile.alias}</small></h2>
          <p>{profile.shortBio}</p>
          <small>{profile.avatarUrl}</small>
        </div>
      </div>
      <hr />
      <h3>Manifest (AI quick)</h3>
      <small>Wygeneruj manifest AI na podstawie profilu</small>
      <div style={{marginTop:8}}>
        <button onClick={async ()=>{
          const r = await fetch('/api/ai/manifest', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({prompt: profile.shortBio})});
          const j = await r.json();
          alert('Manifest:\n\n' + j.manifest);
        }}>Wygeneruj manifest</button>
      </div>
    </div>
  )
}