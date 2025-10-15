export class PurgeEngine {
  purge(profile: any) {
    if (profile.trustScore < 0.3 || profile.activity < 1) {
      console.log(`🧹 Purged account: ${profile.id}`);
      return true;
    }
    return false;
  }
}
