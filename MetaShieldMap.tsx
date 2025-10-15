import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import React from 'react';

export const MetaShieldMap = ({ threats }: { threats: any[] }) => (
  <MapContainer center={[52, 21]} zoom={5} style={{ height: '400px', width: '100%' }}>
    <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
    {threats.map((t, i) => (
      <Marker key={i} position={[t.lat, t.lon]}>
        <Popup>{t.profileId}</Popup>
      </Marker>
    ))}
  </MapContainer>
);
