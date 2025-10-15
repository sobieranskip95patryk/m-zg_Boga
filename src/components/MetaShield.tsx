// MetaShield.tsx
// Interfejs dla AnonymousAgent 2.0 + SkyHeart

import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

type ThreatEntry = {
  id: string;
  username: string;
  reason: string;
  location: string;
  emotion: string;
  intensity: number;
};

const MetaShield: React.FC = () => {
  const [threats, setThreats] = useState<ThreatEntry[]>([]);

  useEffect(() => {
    // Symulacja pobierania danych z AnonymousAgent
    const fetchThreats = async () => {
      const mockData: ThreatEntry[] = [
        {
          id: "user123",
          username: "CryptoScammer01",
          reason: "Suspicious activity",
          location: "Lagos, Nigeria",
          emotion: "anger",
          intensity: 0.85
        },
        {
          id: "user456",
          username: "BotTraderX",
          reason: "Manipulative message detected",
          location: "Moscow, Russia",
          emotion: "neutral",
          intensity: 0.4
        }
      ];
      setThreats(mockData);
    };

    fetchThreats();
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>🛡️ MetaShield — Dashboard Zagrożeń</h1>
      <p>Monitorowanie podejrzanych kont, emocji i lokalizacji IP</p>

      <div style={{ marginTop: "2rem" }}>
        <MapContainer center={[20, 0]} zoom={2} style={{ height: "400px", width: "100%" }}>
          <TileLayer
            attribution='&copy; OpenStreetMap'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {threats.map((entry, index) => (
            <Marker key={index} position={[Math.random() * 60 - 30, Math.random() * 120 - 60]}>
              <Popup>
                <strong>{entry.username}</strong><br />
                {entry.reason}<br />
                Emotion: {entry.emotion} ({entry.intensity})
              </Popup>
            </Marker>
          ))}
        </MapContainer>
      </div>

      <div style={{ marginTop: "2rem" }}>
        <h2>📋 Lista Podejrzanych Kont</h2>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Username</th>
              <th>Reason</th>
              <th>Location</th>
              <th>Emotion</th>
              <th>Intensity</th>
            </tr>
          </thead>
          <tbody>
            {threats.map((entry) => (
              <tr key={entry.id}>
                <td>{entry.id}</td>
                <td>{entry.username}</td>
                <td>{entry.reason}</td>
                <td>{entry.location}</td>
                <td>{entry.emotion}</td>
                <td>{entry.intensity}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MetaShield;
