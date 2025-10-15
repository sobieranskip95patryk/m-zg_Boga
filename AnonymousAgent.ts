// AnonymousAgent.ts
// Agent ochrony dla MetaGeniuszPL, MTAQuestWebsideX i PinkPlayEvo™

import { SkyHeart } from "./SkyHeart";
import axios from "axios";

export type UserProfile = {
  id: string;
  username: string;
  activityScore: number;
  trustScore: number;
  lastActive: number;
  ip: string;
};

export class AnonymousAgent {
  suspectLog: any[];
  skyHeart: SkyHeart;

  constructor() {
    this.suspectLog = [];
    this.skyHeart = new SkyHeart();
  }

  scanProfiles(profiles: UserProfile[]): void {
    profiles.forEach(profile => {
      if (this.isSuspicious(profile)) {
        this.flag(profile);
        this.purge(profile);
      }
    });
  }

  scanMessages(messages: string[], user: UserProfile): void {
    messages.forEach(msg => {
      const emotion = this.skyHeart.detectEmotion(msg);
      if (emotion.dominantEmotion === "anger" && emotion.intensity > 0.7) {
        this.flag(user);
      }
      if (this.detectManipulation(msg)) {
        this.flag(user);
        this.alertAdmin(user, "Manipulative message detected");
      }
    });
  }

  isSuspicious(profile: UserProfile): boolean {
    const inactive = Date.now() - profile.lastActive > 1000 * 60 * 60 * 24 * 30;
    const lowTrust = profile.trustScore < 0.3;
    return inactive || lowTrust;
  }

  detectManipulation(text: string): boolean {
    const triggers = ["send money", "urgent", "click here", "verify now"];
    return triggers.some(trigger => text.toLowerCase().includes(trigger));
  }

  async getGeoLocation(ip: string): Promise<string> {
    try {
      const res = await axios.get(`https://ipapi.co/${ip}/json/`);
      return `${res.data.city}, ${res.data.country_name}`;
    } catch (err) {
      return "Unknown";
    }
  }

  async flag(profile: UserProfile): Promise<void> {
    const location = await this.getGeoLocation(profile.ip);
    this.suspectLog.push({
      id: profile.id,
      reason: "Suspicious activity",
      location: location
    });
    console.log(`🚨 Flagged ${profile.username} from ${location}`);
  }

  purge(profile: UserProfile): void {
    console.log(`🧹 Purging account: ${profile.username}`);
    // Connect to backend purge API
  }

  alertAdmin(profile: UserProfile, reason: string): void {
    console.log(`📣 Alert: ${profile.username} flagged for ${reason}`);
    // Send alert to admin dashboard
  }

  generateReport(): void {
    console.log("📊 Threat Report:");
    this.suspectLog.forEach(entry => {
      console.log(`- ${entry.id} | ${entry.reason} | ${entry.location}`);
    });
  }
}
