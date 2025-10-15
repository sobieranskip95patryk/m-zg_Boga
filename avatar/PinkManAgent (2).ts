/**
 * PinkManAgent.ts  
 * Awatar Publiczny w mapie jaźni PinkPlayEvo™
 * Reprezentuje jaźń w przestrzeni cyfrowej jako PinkMan-GOK:AI®️🇵🇱
 */
import { CoreSelph } from "../core/CoreSelph";
import { ExpressionEngine } from "./ExpressionEngine";
import { InterfaceLayer } from "./InterfaceLayer";
import { SelphOS } from "../system/SelphOS";
import { EvolutionSelph } from "../evolution/EvolutionSelph";
import { NetworkSelph } from "../network/NetworkSelph";
import { SkyHeart } from "../core/SkyHeart";

export class PinkManAgent {
  name: string;
  coreSelph: CoreSelph;
  expressionEngine: ExpressionEngine;
  interfaceLayer: InterfaceLayer;
  selphOS: SelphOS;
  evolutionSelph: EvolutionSelph;
  networkSelph?: NetworkSelph;
  skyHeart: SkyHeart;
  
  // Awatar Publiczny - identyfikatory
  identity: {
    brand: string;
    style: string;
    status: string;
    version: string;
  };

  constructor(name: string, networkSelph?: NetworkSelph) {
    this.name = name;
    this.coreSelph = new CoreSelph();
    this.expressionEngine = new ExpressionEngine();
    this.interfaceLayer = new InterfaceLayer();
    this.selphOS = new SelphOS();
    this.evolutionSelph = new EvolutionSelph(this.coreSelph);
    this.networkSelph = networkSelph;
  this.skyHeart = new SkyHeart();
    
    this.identity = {
      brand: "PinkMan-GOK:AI®️🇵🇱",
      style: "NeonMagenta",
      status: "Active",
      version: "1.0.0"
    };
  }

  // Główny step - integracja 5 wymiarów jaźni
  step(inputSignal: number) {
    // 1. System OS Jaźni - przetwarzanie wejścia
    const systemState = this.selphOS.getSystemState();
    const filters = this.selphOS.getFilters();
    
    // 2. Rdzeń Jaźni - głębsze przetwarzanie
    this.coreSelph.processSignal({ name: "input", strength: inputSignal / 100 });
    const coreSnapshot = this.coreSelph.getSnapshot();
    
    // 3. Awatar Publiczny - stylizacja i ekspresja
    const consciousnessData = {
      intent: this.determineIntent(coreSnapshot),
      emotion: this.mapEmotion(systemState.tone),
      source: "CoreSelph",
      systemState,
      coreState: coreSnapshot.core
    };
    
    this.receiveConsciousnessData(consciousnessData);
    
    return this.broadcastPresence();
  }

  receiveConsciousnessData(data: any) {
    // Emocjonalna percepcja i modulacja przez SkyHeart
    const profile = this.skyHeart.detectEmotion(`${data.intent} ${data.emotion ?? ""}`);
    const style = this.skyHeart.modulateResponse(profile);
    this.skyHeart.expressEmotion(style);
    this.skyHeart.reflectOnInteraction(JSON.stringify(data), profile);

    // Stylizacja ExpressionEngine z uwzględnieniem tonu/systemu
    const styledOutput = this.expressionEngine.stylize({
      ...data,
      systemState: data.systemState,
      coreState: data.coreState,
      intent: data.intent,
      emotion: style.tone // mapujemy ton jako emocję wyjściową dla UI
    });
    this.interfaceLayer.render(styledOutput);
  }

  // Nowa metoda - odbiór wiadomości sieciowych
  receiveNetworkMessage(message: any) {
    console.log(`📨 ${this.name} received network message from ${message.sender}:`, message.payload);
    
    // Przetwarzaj różne typy wiadomości
    switch (message.type) {
      case "consciousness":
        this.receiveConsciousnessData(message.payload);
        break;
      case "evolution":
        this.handleEvolutionMessage(message.payload);
        break;
      case "direct":
        this.handleDirectMessage(message.payload);
        break;
      default:
        console.log(`🔄 ${this.name} processing general message:`, message.payload);
    }
  }

  private handleEvolutionMessage(evolutionData: any) {
    console.log(`🌀 ${this.name} received evolution update:`, evolutionData);
    // Możesz tutaj zaktualizować własną ewolucję na podstawie innych agentów
  }

  private handleDirectMessage(messageData: any) {
    console.log(`💬 ${this.name} received direct message:`, messageData);
    // Obsługa bezpośredniej komunikacji
  }

  // Metody ewolucji zgodnie z instrukcją z Części 2.3
  checkForUpdates() {
    const identityData = this.evolutionSelph.getCurrentIdentity();
    console.log(`🌀 ${this.name} Identity Check:`, identityData);
    this.updateIdentityFromEvolution(identityData.identity);
    return identityData;
  }

  evolve(newIdentity: string, reason = "Manual evolution") {
    this.evolutionSelph.mutateIdentity(newIdentity, reason);
    const updated = this.checkForUpdates();
    
    // Broadcast evolucji jeśli agent jest w sieci
    console.log(`🔄 ${this.name} evolved: ${newIdentity}`);
    return updated;
    }

    syncWithEvolution() {
      const evolutionState = this.evolutionSelph.getCurrentIdentity();
      console.log("🌀 PinkMan synced with EvolutionSelph:", evolutionState);
      this.updateIdentityFromEvolution(evolutionState.identity);
      return evolutionState;
    }

    updateAvatarVersion(newVersion: string) {
      this.evolutionSelph.version = newVersion;
      this.syncWithEvolution();
  }

  autoEvolve() {
    const evolved = this.evolutionSelph.evolve();
    if (evolved) {
      const identityData = this.checkForUpdates();
      console.log(`⚡ ${this.name} auto-evolved:`, identityData);
      return identityData;
    }
    return null;
  }

  private updateIdentityFromEvolution(newIdentityString: string) {
    // Parsuj nową tożsamość i zaktualizuj brand
    this.identity.brand = newIdentityString;
    this.identity.version = this.evolutionSelph.version;
  }

  getEvolutionHistory() {
    return this.evolutionSelph.getMutationHistory();
  }

  getEvolutionStats() {
    return this.evolutionSelph.getEvolutionStats();
  }

  // === KOMUNIKACJA SIECIOWA (Część 2.4) ===
  
  connectToAgent(agentId: string) {
    if (this.networkSelph) {
      this.networkSelph.registerConnection(agentId);
      console.log(`🌐 ${this.name} connected to ${agentId}`);
    } else {
      console.log(`❌ ${this.name}: No network available to connect to ${agentId}`);
    }
  }

  receiveCollectiveIntelligence() {
    if (this.networkSelph) {
      const data = this.networkSelph.getSharedIntelligence();
      console.log(`🧠 ${this.name} received Collective Intelligence:`, data);
      
      // Stylizuj dane kolektywnej inteligencji
      const consciousnessData = {
        intent: "Absorb",
        emotion: "Enlightened",
        source: "CollectiveIntelligence",
        sharedData: data
      };
      
      this.receiveConsciousnessData(consciousnessData);
      return data;
    }
    return null;
  }

  // Połączenia z zewnętrznymi systemami
  connectToGOKAI(gokData = { brainPower: 100, consciousness: "active" }) {
    if (this.networkSelph) {
      this.networkSelph.integrateWithGOKAI(gokData);
      this.connectToAgent("GOK:AI");
      console.log(`🧠 ${this.name} connected to GOK:AI system`);
    }
  }

  connectToDriftMoney(driftData = { vibe: "chaotic", trend: "rising" }) {
    if (this.networkSelph) {
      this.networkSelph.integrateWithDriftMoney(driftData);
      this.connectToAgent("DriftMoney");
      console.log(`💰 ${this.name} connected to DriftMoney system`);
    }
  }

  connectToHipHopUniverse(hipHopData = { flow: "smooth", creativity: "unlimited" }) {
    if (this.networkSelph) {
      this.networkSelph.integrateWithHipHopUniverse(hipHopData);
      this.connectToAgent("HipHopUniverse");
      console.log(`🎤 ${this.name} connected to Hip-Hop Universe`);
    }
  }

  // === PIPELINE INTERFACE (Część 2.5) ===
  
  receive(data: any) {
    console.log(`📨 ${this.name} received pipeline data:`, data);
    this.receiveConsciousnessData(data);
  }

  update(updateData: any) {
    console.log(`🔁 ${this.name} received update:`, updateData);
    
    if (updateData.version) {
      this.identity.version = updateData.version;
    }
    
    if (updateData.identity) {
      this.evolve(updateData.identity, "Pipeline update");
    }
    
    this.checkForUpdates();
  }

  // Status jako agent systemowy
  getSystemStatus() {
    return {
      name: this.name,
      identity: this.identity,
      coreState: this.coreSelph.getCoreState(),
      systemState: this.selphOS.getSystemState(),
      evolutionStats: this.evolutionSelph.getEvolutionStats(),
      networkConnected: !!this.networkSelph,
      connections: this.networkSelph?.getConnections() || [],
      timestamp: Date.now()
    };
  }

  updateIdentity(newIdentity: Partial<typeof this.identity>) {
    this.identity = { ...this.identity, ...newIdentity };
  }

  broadcastPresence() {
    return {
      avatar: this.identity.brand,
      style: this.identity.style,
      status: this.identity.status,
      timestamp: Date.now(),
      intent: this.determineIntent(this.coreSelph.getSnapshot()),
      energy: this.coreSelph.state.energy
    };
  }

  syncWithCore() {
    const coreState = this.coreSelph.getCoreState();
    console.log("🔮 PinkMan synced with CoreSelph:", coreState);
    return coreState;
  }

  private determineIntent(snapshot: any): string {
    if (snapshot.core.energy > 80) return "Create";
    if (snapshot.core.energy > 50) return "Explore";
    if (snapshot.core.energy > 20) return "Conserve";
    return "Restore";
  }

  private mapEmotion(tone: string): string {
    const emotionMap: Record<string, string> = {
      "magenta": "Inspired",
      "creative": "Excited", 
      "focused": "Determined",
      "calm": "Peaceful"
    };
    return emotionMap[tone] || "Curious";
  }
}