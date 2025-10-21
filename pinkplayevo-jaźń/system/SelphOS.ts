/**
 * SelphOS.ts
 * System Operacyjny Jaźni w mapie PinkPlayEvo™
 * Logika, filtry percepcji, mechanizmy decyzyjne
 */
import { CoreSelph } from "../core/CoreSelph";
import { ConsciousKernel } from "./ConsciousKernel";

export interface SelphState {
  mode: "creative" | "logical" | "intuitive" | "social" | "evolutionary";
  focus: "transformation" | "exploration" | "connection" | "creation" | "conservation";
  tone: "magenta" | "creative" | "focused" | "calm" | "energetic";
  adaptationLevel: number;
  environment: "online" | "offline" | "hybrid";
}

export interface PerceptionFilter {
  name: string;
  active: boolean;
  intensity: number;
  purpose: string;
}

export class SelphOS {
  state: SelphState;
  filters: PerceptionFilter[];
  kernel: ConsciousKernel;
  
  constructor() {
    this.state = {
      mode: "creative",
      focus: "transformation",
      tone: "magenta",
      adaptationLevel: 0.7,
      environment: "hybrid"
    };
    
    this.filters = [
      { name: "intuition", active: true, intensity: 0.8, purpose: "wisdom_detection" },
      { name: "logic", active: true, intensity: 0.6, purpose: "pattern_analysis" },
      { name: "emotion", active: true, intensity: 0.9, purpose: "resonance_sensing" },
      { name: "creativity", active: true, intensity: 1.0, purpose: "possibility_expansion" },
      { name: "social", active: true, intensity: 0.5, purpose: "connection_mapping" }
    ];
    
    this.kernel = new ConsciousKernel(this);
  }

  getSystemState(): SelphState {
    return { ...this.state };
  }

  getFilters(): PerceptionFilter[] {
    return [...this.filters];
  }

  // Główna funkcja decyzyjna systemu
  processInput(input: any): any {
    // 1. Filtrowanie percepcji
    const filteredInput = this.applyFilters(input);
    
    // 2. Adaptacja do środowiska
    this.adaptToEnvironment();
    
    // 3. Generowanie decyzji przez kernel
    const decision = this.kernel.publishIntent();
    
    // 4. Update stanu systemu
    this.updateState(filteredInput, decision);
    
    return {
      originalInput: input,
      filteredInput,
      decision,
      systemState: this.getSystemState()
    };
  }

  private applyFilters(input: any): any {
    return this.filters
      .filter(filter => filter.active)
      .reduce((processed, filter) => {
        return this.applyFilter(processed, filter);
      }, input);
  }

  private applyFilter(data: any, filter: PerceptionFilter): any {
    switch (filter.name) {
      case "intuition":
        return { ...data, intuition: data.strength * filter.intensity };
      case "logic":
        return { ...data, logic: Math.round(data.strength * filter.intensity * 10) / 10 };
      case "emotion":
        return { ...data, emotion: this.mapEmotionalResonance(data, filter.intensity) };
      case "creativity":
        return { ...data, creativity: this.expandPossibilities(data, filter.intensity) };
      case "social":
        return { ...data, social: this.mapSocialContext(data, filter.intensity) };
      default:
        return data;
    }
  }

  private adaptToEnvironment() {
    const hour = new Date().getHours();
    
    // Adaptacja do cyklu dobowego
    if (hour >= 22 || hour <= 6) {
      this.state.mode = "intuitive";
      this.state.tone = "calm";
    } else if (hour >= 9 && hour <= 17) {
      this.state.mode = "logical";
      this.state.tone = "focused";
    } else {
      this.state.mode = "creative";
      this.state.tone = "energetic";
    }
  }

  private updateState(input: any, decision: any) {
    // Ewolucja poziomu adaptacji
    if (decision.intent === "Create") {
      this.state.adaptationLevel = Math.min(1.0, this.state.adaptationLevel + 0.01);
    }
    
    // Przełączanie fokusa na podstawie wzorców
    if (input.strength > 80) {
      this.state.focus = "creation";
    } else if (input.social && input.social.connections > 0) {
      this.state.focus = "connection";
    }
  }

  // Funkcje pomocnicze filtrów
  private mapEmotionalResonance(data: any, intensity: number): any {
    return {
      resonance: data.strength * intensity,
      valence: data.strength > 50 ? "positive" : "neutral"
    };
  }

  private expandPossibilities(data: any, intensity: number): any {
    return {
      potential: Math.round(data.strength * intensity * 1.5),
      variants: Math.floor(intensity * 3)
    };
  }

  private mapSocialContext(data: any, intensity: number): any {
    return {
      connections: Math.floor(intensity * 2),
      collaboration: data.strength * intensity > 60
    };
  }

  // API do kontroli systemu
  activateFilter(filterName: string) {
    const filter = this.filters.find(f => f.name === filterName);
    if (filter) filter.active = true;
  }

  deactivateFilter(filterName: string) {
    const filter = this.filters.find(f => f.name === filterName);
    if (filter) filter.active = false;
  }

  adjustFilterIntensity(filterName: string, intensity: number) {
    const filter = this.filters.find(f => f.name === filterName);
    if (filter) filter.intensity = Math.max(0, Math.min(1, intensity));
  }

  switchMode(newMode: SelphState["mode"]) {
    this.state.mode = newMode;
    this.adaptFiltersToMode();
  }

  private adaptFiltersToMode() {
    switch (this.state.mode) {
      case "creative":
        this.adjustFilterIntensity("creativity", 1.0);
        this.adjustFilterIntensity("logic", 0.4);
        break;
      case "logical":
        this.adjustFilterIntensity("logic", 1.0);
        this.adjustFilterIntensity("emotion", 0.3);
        break;
      case "intuitive":
        this.adjustFilterIntensity("intuition", 1.0);
        this.adjustFilterIntensity("logic", 0.2);
        break;
      case "social":
        this.adjustFilterIntensity("social", 1.0);
        this.adjustFilterIntensity("emotion", 0.9);
        break;
      case "evolutionary":
        // Wszystkie filtry równomiernie
        this.filters.forEach(f => f.intensity = 0.7);
        break;
    }
  }

  snapshot(): any {
    return {
      state: this.getSystemState(),
      filters: this.getFilters(),
      decision: this.kernel.publishIntent(),
      timestamp: Date.now()
    };
  }

  // Pipeline interface
  receive(data: any) {
    console.log("🖥️ SelphOS received pipeline data:", data);
    
    // Przetwarzaj dane przez system filtrów
    const processed = this.processInput(data);
    console.log("🔍 SelphOS processed:", processed);
  }

  update(updateData: any) {
    console.log("🔄 SelphOS received update:", updateData);
    
    if (updateData.mode) {
      this.switchMode(updateData.mode);
    }
    
    if (updateData.filters) {
      Object.entries(updateData.filters).forEach(([filterName, intensity]) => {
        this.adjustFilterIntensity(filterName, intensity as number);
      });
    }
  }
}