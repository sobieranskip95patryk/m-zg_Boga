export class ReportInterface {
  generateReport(profile: any, reason: string) {
    return {
      id: profile.id,
      status: "flagged",
      reason,
      timestamp: Date.now()
    };
  }
  alertAdmin(profileId: string, message: string) {
    console.log(`🚨 Alert for admin: ${profileId} — ${message}`);
  }
}
