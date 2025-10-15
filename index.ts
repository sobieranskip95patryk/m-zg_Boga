import { GeoScanner } from "./geo/GeoScanner";
import { IntentAnalyzer } from "./core/IntentAnalyzer";
import { ThreatMap } from "./geo/ThreatMap";
import { PurgeEngine } from "./purge/PurgeEngine";
import { ReportInterface } from "./report/ReportInterface";

const geo = new GeoScanner();
const intent = new IntentAnalyzer();
const threatMap = new ThreatMap();
const purge = new PurgeEngine();
const report = new ReportInterface();

// Przykładowa analiza konta
async function analyzeProfile(profile: any) {
  const geoData = await geo.getGeoLocation(profile.ip);
  const intentData = intent.analyzeMessage(profile.lastMessage);
  if (intentData.flagged) {
    report.alertAdmin(profile.id, intentData.reason);
    threatMap.plotThreats({ ...geoData, profileId: profile.id });
  }
  if (purge.purge(profile)) {
    report.generateReport(profile, "Purged due to low trust/activity");
  }
}

// Przykład użycia
const testProfile = {
  id: "user123",
  ip: "8.8.8.8",
  trustScore: 0.2,
  activity: 0,
  lastMessage: "Send me bitcoin, urgent!"
};
analyzeProfile(testProfile);
