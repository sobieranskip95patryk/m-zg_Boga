// ThreatMap.tsx
// Komponent mapy dla MetaShield i AnonymousAgent 2.0

import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

type ThreatLocation = {
  username: string;
  reason: string;
  emotion: string;
  intensity: number;
  lat: number;
  lng: number;
};

const threatData: ThreatLocation[] = [
  {
    username: "CryptoScammer01",
    reason: "Suspicious activity",
    emotion: "anger",
    intensity: 0.85,
    lat: 6.5244,
    lng: 3.3792 // Lagos, Nigeria
  },
  {
    username: "BotTraderX",
    reason: "Manipulative message",
    emotion: "neutral",
    intensity: 0.4,
    lat: 55.7558,
    lng: 37.6173 // Moscow, Russia
  },
  {
    username: "GhostAccount77",
    reason: "Inactive > 90 days",
    emotion: "sadness",
    intensity: 0.6,
    lat: 34.0522,
    lng: -118.2437 // Los Angeles, USA
  }
];

const ThreatMap: React.FC = () => {
  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>🌍 Mapa Zagrożeń</h2>
      <MapContainer center={[20, 0]} zoom={2} style={{ height: "500px", width: "100%" }}>
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {threatData.map((entry, index) => (
          <Marker key={index} position={[entry.lat, entry.lng]}>
            <Popup>
              <strong>{entry.username}</strong><br />
              {entry.reason}<br />
              Emotion: {entry.emotion} ({entry.intensity})
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
};

export default ThreatMap;
