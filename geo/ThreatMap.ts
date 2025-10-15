export class ThreatMap {
  threats: any[] = [];
  plotThreats(threat: any) {
    this.threats.push(threat);
    // Tu można podpiąć mapę Leaflet.js/React do wizualizacji
    console.log("🗺️ Threat mapped:", threat);
  }
}
