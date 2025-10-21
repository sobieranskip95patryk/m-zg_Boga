/**
 * CoreSelph.ts
 * Rdzeń świadomości - Deep Selph w mapie jaźni PinkPlayEvo™
 * Intuicja, obecność, źródło wszystkich procesów mentalnych
 */
import { IntuitionModule, Signal } from "./IntuitionModule";

export interface CoreState {
  presence: "active" | "dormant" | "focused" | "distributed";
  intuition: "aligned" | "conflicted" | "seeking" | "crystallized";
  energy: number;
  depth: number;
}

export class CoreSelph {
  state: CoreState;
  intuitionModule: IntuitionModule;

  constructor() {
    this.state = {
      presence: "active",
      intuition: "aligned", 
      energy: 100,
      depth: 1
    };
    this.intuitionModule = new IntuitionModule();
  }

  getCoreState(): CoreState {
    return { ...this.state };
  }

  getSnapshot() {
    return {
      core: this.getCoreState(),
      intuition: this.intuitionModule.decide(),
      timestamp: Date.now()
    };
  }

  processSignal(signal: Signal) {
    this.intuitionModule.registerSignal(signal);
    this.state.energy = Math.max(0, this.state.energy - 1);
  }

  deepFocus() {
    this.state.presence = "focused";
    this.state.depth += 0.1;
  }

  restore() {
    this.state.energy = Math.min(100, this.state.energy + 10);
    this.state.presence = "active";
  }

  // Pipeline interface
  receive(data: any) {
    console.log("🔮 CoreSelph received pipeline data:", data);
    
    if (data.type === "signal" || data.intent) {
      this.processSignal({ 
        name: data.intent || "pipeline_signal", 
        strength: data.energy ? data.energy / 100 : 0.5 
      });
    }
  }

  update(updateData: any) {
    console.log("🔄 CoreSelph received update:", updateData);
    
    if (updateData.energy !== undefined) {
      this.state.energy = Math.max(0, Math.min(100, updateData.energy));
    }
    
    if (updateData.presence) {
      this.state.presence = updateData.presence;
    }
  }
}