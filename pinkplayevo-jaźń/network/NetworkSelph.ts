/**
 * NetworkSelph.ts
 * Jaźń Sieciowa w mapie PinkPlayEvo™
 * Relacje, AI, kolektywna świadomość, komunikacja między agentami
 */
import { PinkManAgent } from "../avatar/PinkManAgent";
import { RelationEngine } from "./RelationEngine";

export interface NetworkMessage {
  sender: string;
  receiver: string;
  payload: any;
  timestamp: number;
  type: "broadcast" | "direct" | "evolution" | "consciousness";
}

export class NetworkSelph {
  peers: PinkManAgent[] = [];
  relationEngine: RelationEngine;
  messageHistory: NetworkMessage[] = [];
  private maxHistory = 1000;
  
  // Nowe właściwości zgodnie z instrukcją
  connections: any[] = [];
  sharedIntelligence: Record<string, any> = {};

  constructor() {
    this.relationEngine = new RelationEngine();
  }

  // Nowe metody zgodnie z instrukcją
  registerConnection(agentId: string) {
    this.connections.push({
      id: agentId,
      timestamp: Date.now(),
      status: "active"
    });
    console.log(`🔗 NetworkSelph: Registered connection to ${agentId}`);
  }

  getConnections() {
    return [...this.connections];
  }

  updateSharedIntelligence(source: string, data: any) {
    this.sharedIntelligence[source] = {
      ...data,
      timestamp: Date.now(),
      source
    };
    console.log(`🧠 NetworkSelph: Updated shared intelligence from ${source}:`, data);
  }

  getSharedIntelligence() {
    return { ...this.sharedIntelligence };
  }

  register(agent: PinkManAgent) {
    this.peers.push(agent);
    console.log(`🌐 NetworkSelph: Registered agent ${agent.name}`);
  }

  unregister(agentName: string) {
    this.peers = this.peers.filter(p => p.name !== agentName);
    console.log(`🌐 NetworkSelph: Unregistered agent ${agentName}`);
  }

  broadcast(sender: PinkManAgent, payload: any, type: NetworkMessage["type"] = "broadcast") {
    const message: NetworkMessage = {
      sender: sender.name,
      receiver: "*all*",
      payload,
      timestamp: Date.now(),
      type
    };

    this.messageHistory.push(message);
    this.maintainHistory();

    for (const peer of this.peers) {
      if (peer.name !== sender.name) {
        // Strengthen relation through interaction
        this.relationEngine.strengthen(sender.name, peer.name, 0.05);
        
        // Log with relation strength
        const relation = this.relationEngine.getRelation(sender.name, peer.name);
        console.log(`[net] ${sender.name} -> ${peer.name} (bond: ${relation.weight.toFixed(2)}):`, payload);
        
        // Jeśli peer ma metodę otrzymywania wiadomości
        if (typeof peer.receiveNetworkMessage === 'function') {
          peer.receiveNetworkMessage(message);
        }
      }
    }

    return message;
  }

  sendDirect(sender: PinkManAgent, receiverName: string, payload: any) {
    const receiver = this.peers.find(p => p.name === receiverName);
    if (!receiver) {
      console.log(`❌ NetworkSelph: Receiver ${receiverName} not found`);
      return null;
    }

    const message: NetworkMessage = {
      sender: sender.name,
      receiver: receiverName,
      payload,
      timestamp: Date.now(),
      type: "direct"
    };

    this.messageHistory.push(message);
    this.maintainHistory();

    // Strengthen relation more for direct communication
    this.relationEngine.strengthen(sender.name, receiverName, 0.1);

    const relation = this.relationEngine.getRelation(sender.name, receiverName);
    console.log(`[direct] ${sender.name} -> ${receiverName} (bond: ${relation.weight.toFixed(2)}):`, payload);

    if (typeof receiver.receiveNetworkMessage === 'function') {
      receiver.receiveNetworkMessage(message);
    }

    return message;
  }

  // Broadcast ewolucji tożsamości
  broadcastEvolution(sender: PinkManAgent, evolutionData: any) {
    return this.broadcast(sender, evolutionData, "evolution");
  }

  // Broadcast danych świadomościowych
  broadcastConsciousness(sender: PinkManAgent, consciousnessData: any) {
    return this.broadcast(sender, consciousnessData, "consciousness");
  }

  // Analiza sieci i relacji
  getNetworkAnalysis() {
    const activeAgents = this.peers.length;
    const totalMessages = this.messageHistory.length;
    const relations = this.relationEngine.relations;
    
    // Znajdź najsilniejsze relacje
    const strongestRelations = relations
      .sort((a, b) => b.weight - a.weight)
      .slice(0, 5);

    // Statystyki komunikacji
    const messagesByType = this.messageHistory.reduce((acc, msg) => {
      acc[msg.type] = (acc[msg.type] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);

    return {
      activeAgents,
      totalMessages,
      totalRelations: relations.length,
      strongestRelations,
      messagesByType,
      networkHealth: this.calculateNetworkHealth()
    };
  }

  private calculateNetworkHealth(): number {
    if (this.peers.length === 0) return 0;
    
    const avgRelationStrength = this.relationEngine.relations.length > 0 
      ? this.relationEngine.relations.reduce((sum, r) => sum + r.weight, 0) / this.relationEngine.relations.length
      : 0;
    
    const activityScore = Math.min(1, this.messageHistory.length / 100);
    
    return (avgRelationStrength * 0.7 + activityScore * 0.3);
  }

  // Czyszczenie i utrzymanie historii
  private maintainHistory() {
    if (this.messageHistory.length > this.maxHistory) {
      this.messageHistory = this.messageHistory.slice(-this.maxHistory);
    }
  }

  clearHistory() {
    this.messageHistory = [];
  }

  // API do pobierania danych
  getMessageHistory(): NetworkMessage[] {
    return [...this.messageHistory];
  }

  getRelations() {
    return this.relationEngine.relations;
  }

  getPeers(): PinkManAgent[] {
    return [...this.peers];
  }

  // Znajdowanie agentów
  findAgent(name: string): PinkManAgent | undefined {
    return this.peers.find(p => p.name === name);
  }

  // Synchronizacja stanu sieci
  syncNetworkState() {
    const networkState = {
      analysis: this.getNetworkAnalysis(),
      timestamp: Date.now()
    };

    this.broadcast(
      { name: "NetworkSelph", broadcastPresence: () => ({}) } as PinkManAgent,
      networkState,
      "consciousness"
    );

    return networkState;
  }

  // Metody do zarządzania kolektywną inteligencją
  connectToExternalSystem(systemName: string, systemData: any) {
    this.registerConnection(systemName);
    this.updateSharedIntelligence(systemName, systemData);
    
    // Powiadom wszystkich agentów o nowym połączeniu
    this.broadcast(
      { name: "NetworkSelph", broadcastPresence: () => ({}) } as PinkManAgent,
      { 
        type: "system_connected", 
        system: systemName, 
        data: systemData 
      },
      "consciousness"
    );
  }

  // Integracja z zewnętrznymi systemami (GOK:AI, DriftMoney, Hip-Hop Universe)
  integrateWithGOKAI(gokData: any) {
    this.updateSharedIntelligence("GOK:AI", {
      brainPower: gokData.brainPower || 100,
      consciousness: gokData.consciousness || "active",
      wisdom: gokData.wisdom || "deep"
    });
  }

  integrateWithDriftMoney(driftData: any) {
    this.updateSharedIntelligence("DriftMoney", {
      vibe: driftData.vibe || "chaotic",
      trend: driftData.trend || "rising",
      energy: driftData.energy || "high"
    });
  }

  integrateWithHipHopUniverse(hipHopData: any) {
    this.updateSharedIntelligence("HipHopUniverse", {
      flow: hipHopData.flow || "smooth",
      beats: hipHopData.beats || "heavy",
      creativity: hipHopData.creativity || "unlimited"
    });
  }

  // API do obsługi pipeline
  receive(data: any) {
    console.log("🌐 NetworkSelph received pipeline data:", data);
    
    // Przekaż dane do wszystkich połączonych agentów
    this.broadcast(
      { name: "NetworkSelph", broadcastPresence: () => ({}) } as PinkManAgent,
      data,
      "consciousness"
    );
  }

  update(updateData: any) {
    console.log("🔄 NetworkSelph received update:", updateData);
    
    // Aktualizuj stan sieci na podstawie update'u
    if (updateData.version) {
      this.updateSharedIntelligence("SystemUpdate", updateData);
    }
  }
}
