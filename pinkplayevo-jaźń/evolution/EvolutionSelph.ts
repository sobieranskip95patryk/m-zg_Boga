/**
 * EvolutionSelph.ts
 * Jaźń Ewolucyjna w mapie PinkPlayEvo™
 * Transformacja, wersjonowanie, mutacje tożsamości
 */
import { CoreSelph } from "../core/CoreSelph";

export interface MutationLog {
  from: string;
  to: string;
  timestamp: number;
  reason?: string;
}

export class EvolutionSelph {
  version: string;
  identity: string;
  mutationLog: MutationLog[];
  core?: CoreSelph;

  constructor(core?: CoreSelph) {
    this.version = "1.0.0";
    this.identity = "PinkMan-GOK:AI®️🇵🇱";
    this.mutationLog = [];
    this.core = core;
  }

  getCurrentIdentity() {
    return {
      version: this.version,
      identity: this.identity,
      mutations: this.mutationLog.length
    };
  }

  mutateIdentity(newIdentity: string, reason = "Evolution") {
    this.mutationLog.push({
      from: this.identity,
      to: newIdentity,
      timestamp: Date.now(),
      reason
    });
    this.identity = newIdentity;
    
    // Auto-increment version przy mutacji
    this.bumpVersion();
  }

  getMutationHistory(): MutationLog[] {
    return [...this.mutationLog];
  }

  private bumpVersion() {
    const parts = this.version.split('.');
    const patch = parseInt(parts[2]) + 1;
    this.version = `${parts[0]}.${parts[1]}.${patch}`;
  }

  // Nowa metoda zgodnie z Twoją instrukcją
  proposeMutation(): any {
    if (!this.core) return null;
    
    const coreSnapshot = this.core.getSnapshot();
    const energyLevel = coreSnapshot.core.energy;
    
    // Proponuj mutację na podstawie stanu rdzenia
    if (energyLevel > 80) {
      return {
        type: "identity_boost",
        newIdentity: `${this.identity} ⚡Enhanced`,
        reason: "High energy state"
      };
    } else if (energyLevel < 20) {
      return {
        type: "identity_restore", 
        newIdentity: `${this.identity} 🌱Restored`,
        reason: "Low energy recovery"
      };
    }
    
    return {
      type: "identity_maintain",
      newIdentity: this.identity,
      reason: "Stable state"
    };
  }

  // Evolve na podstawie propozycji
  evolve() {
    const mutation = this.proposeMutation();
    if (mutation && mutation.type !== "identity_maintain") {
      this.mutateIdentity(mutation.newIdentity, mutation.reason);
      return true;
    }
    return false;
  }

  // Reset do bazowej tożsamości
  resetIdentity() {
    this.mutateIdentity("PinkMan-GOK:AI®️🇵🇱", "Reset to base");
  }

  // Statystyki ewolucji
  getEvolutionStats() {
    return {
      currentVersion: this.version,
      currentIdentity: this.identity,
      totalMutations: this.mutationLog.length,
      lastMutation: this.mutationLog[this.mutationLog.length - 1] || null,
      createdAt: this.mutationLog[0]?.timestamp || Date.now()
    };
  }

  // Pipeline interface
  receive(data: any) {
    console.log("🌀 EvolutionSelph received pipeline data:", data);
    
    // Auto-ewolucja na podstawie danych z pipeline
    if (data.type === "evolution_trigger" || (data.energy && data.energy > 90)) {
      const evolved = this.evolve();
      if (evolved) {
        console.log("⚡ EvolutionSelph auto-evolved based on pipeline data");
      }
    }
  }

  update(updateData: any) {
    console.log("🔄 EvolutionSelph received update:", updateData);
    
    if (updateData.identity) {
      this.mutateIdentity(updateData.identity, "Pipeline update");
    }
    
    if (updateData.version) {
      this.version = updateData.version;
    }
  }
}