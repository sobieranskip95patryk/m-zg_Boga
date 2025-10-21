/**
 * EvolutionaryPipeline.ts
 * Główna magistrala danych systemu jaźni PinkPlayEvo™
 * Łączy wszystkie moduły: CoreSelph, SelphOS, EvolutionSelph, NetworkSelph, PinkManAgent
 */
import { EvolutionSelph } from "../evolution/EvolutionSelph";
import { CoreSelph } from "../core/CoreSelph";
import { SelphOS } from "../system/SelphOS";
import { NetworkSelph } from "../network/NetworkSelph";
import { PinkManAgent } from "../avatar/PinkManAgent";

export interface PipelineModule {
  receive?(data: any): void;
  update?(updateData: any): void;
}

export class EvolutionaryPipeline {
  modules: PipelineModule[];
  pipelineHistory: any[] = [];
  private maxHistory = 500;

  constructor(modules: PipelineModule[] = []) {
    this.modules = modules;
    console.log(`🔄 EvolutionaryPipeline initialized with ${modules.length} modules`);
  }

  // Dodawanie modułów
  addModule(module: PipelineModule) {
    this.modules.push(module);
    console.log(`➕ Module added to pipeline. Total: ${this.modules.length}`);
  }

  removeModule(module: PipelineModule) {
    this.modules = this.modules.filter(m => m !== module);
    console.log(`➖ Module removed from pipeline. Total: ${this.modules.length}`);
  }

  // Transmisja danych do wszystkich modułów
  transmit(data: any) {
    const transmissionData = {
      ...data,
      timestamp: Date.now(),
      pipelineId: Math.random().toString(36).substr(2, 9)
    };

    console.log(`📡 Pipeline transmitting:`, transmissionData);

    this.pipelineHistory.push(transmissionData);
    this.maintainHistory();

    this.modules.forEach((module, index) => {
      try {
        if (module && typeof module.receive === 'function') {
          module.receive(transmissionData);
        }
      } catch (error) {
        console.error(`❌ Error in module ${index} during transmission:`, error);
      }
    });

    return transmissionData;
  }

  // Broadcast aktualizacji do wszystkich modułów
  broadcastUpdate(updateData: any) {
    const update = {
      ...updateData,
      timestamp: Date.now(),
      updateId: Math.random().toString(36).substr(2, 9)
    };

    console.log(`📢 Pipeline broadcasting update:`, update);

    this.pipelineHistory.push({ type: 'update', ...update });
    this.maintainHistory();

    this.modules.forEach((module, index) => {
      try {
        if (module && typeof module.update === 'function') {
          module.update(update);
        }
      } catch (error) {
        console.error(`❌ Error in module ${index} during update:`, error);
      }
    });

    return update;
  }

  // Iteracja ewolucyjna (oryginalna funkcjonalność)
  runIteration(core: CoreSelph) {
    const evo = new EvolutionSelph(core);
    const delta = evo.proposeMutation();
    const passed = core.state.energy > 5; // prosty warunek sukcesu
    
    const result = { 
      delta, 
      passed, 
      snapshot: core.getSnapshot(),
      timestamp: Date.now()
    };

    // Przekaż wyniki iteracji przez pipeline
    this.transmit({
      type: "evolution_iteration",
      result,
      source: "EvolutionaryPipeline"
    });

    return result;
  }

  // Kontrola pipeline'u
  pausePipeline() {
    console.log("⏸️ Pipeline paused");
  }

  resumePipeline() {
    console.log("▶️ Pipeline resumed");
  }

  // Analiza pipeline'u
  getPipelineAnalysis() {
    const totalTransmissions = this.pipelineHistory.length;
    const recentActivity = this.pipelineHistory.slice(-10);
    
    const typeStats = this.pipelineHistory.reduce((acc, item) => {
      const type = item.type || 'transmission';
      acc[type] = (acc[type] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);

    return {
      totalModules: this.modules.length,
      totalTransmissions,
      typeStats,
      recentActivity,
      health: this.calculatePipelineHealth()
    };
  }

  private calculatePipelineHealth(): number {
    if (this.modules.length === 0) return 0;
    
    const activityScore = Math.min(1, this.pipelineHistory.length / 100);
    const moduleScore = Math.min(1, this.modules.length / 5);
    
    return (activityScore * 0.6 + moduleScore * 0.4);
  }

  private maintainHistory() {
    if (this.pipelineHistory.length > this.maxHistory) {
      this.pipelineHistory = this.pipelineHistory.slice(-this.maxHistory);
    }
  }

  // Debugowanie
  getHistory() {
    return [...this.pipelineHistory];
  }

  clearHistory() {
    this.pipelineHistory = [];
    console.log("🗑️ Pipeline history cleared");
  }

  getModuleCount() {
    return this.modules.length;
  }
}
