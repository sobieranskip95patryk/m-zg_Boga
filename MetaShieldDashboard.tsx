import React, { useState } from "react";

export const MetaShieldDashboard = () => {
  const [threats, setThreats] = useState<any[]>([]);
  const [profiles, setProfiles] = useState<any[]>([]);

  // Przykładowa funkcja dodania zagrożenia
  const addThreat = (threat: any) => {
    setThreats([...threats, threat]);
  };

  // Przykładowa funkcja czyszczenia kont
  const purgeProfile = (profileId: string) => {
    setProfiles(profiles.filter(p => p.id !== profileId));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>MetaShield™ Dashboard</h1>
      <h2>Zagrożenia</h2>
      <ul>
        {threats.map((t, i) => (
          <li key={i}>{t.profileId} — {t.city}, {t.country}</li>
        ))}
      </ul>
      <h2>Konta</h2>
      <ul>
        {profiles.map((p, i) => (
          <li key={i}>{p.id} <button onClick={() => purgeProfile(p.id)}>Usuń</button></li>
        ))}
      </ul>
    </div>
  );
};
