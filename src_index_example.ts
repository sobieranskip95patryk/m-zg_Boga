/**
 * src_index_example.ts
 * Dashboard MVP - Pełny system jaźni PinkPlayEvo™ w akcji
 * Demonstruje integrację wszystkich modułów przez EvolutionaryPipeline
 */
import { PinkManAgent } from './avatar/PinkManAgent';
import { NetworkSelph } from './network/NetworkSelph';
import { EvolutionaryPipeline } from './pipeline/EvolutionaryPipeline';
import { CoreSelph } from './core/CoreSelph';
import { SelphOS } from './system/SelphOS';
import { EvolutionSelph } from './evolution/EvolutionSelph';

async function main() {
  console.log("🚀 PinkPlayEvo™ Jaźń System Dashboard MVP - Starting...\n");

  // === INICJALIZACJA SYSTEMU ===
  
  // 1. Tworzenie infrastruktury sieciowej
  const networkSelph = new NetworkSelph();
  
  // 2. Tworzenie agentów z siecią
  const alice = new PinkManAgent('alice', networkSelph);
  const bob = new PinkManAgent('bob', networkSelph);
  
  // 3. Rejestracja w sieci
  networkSelph.register(alice);
  networkSelph.register(bob);
  
  // 4. Utworzenie pipeline'u z wszystkimi modułami
  const pipeline = new EvolutionaryPipeline([
    alice,
    bob,
    alice.coreSelph,
    alice.selphOS,
    alice.evolutionSelph,
    bob.coreSelph, 
    bob.selphOS,
    bob.evolutionSelph,
    networkSelph
  ]);

  console.log("✅ System initialized with full pipeline integration\n");

  // === POŁĄCZENIA Z ZEWNĘTRZNYMI SYSTEMAMI ===
  
  alice.connectToGOKAI({ brainPower: 95, consciousness: "deep" });
  bob.connectToDriftMoney({ vibe: "chaotic", trend: "rising" });
  alice.connectToHipHopUniverse({ flow: "legendary", creativity: "unlimited" });
  
  console.log("\n🌐 External systems connected\n");

  // === DEMO PIPELINE'U ===
  
  for (let i = 0; i < 5; i++) {
    console.log(`\n📊 === Dashboard Iteration ${i + 1} ===`);
    
    // 1. Transmisja danych przez pipeline
    pipeline.transmit({
      type: "consciousness_wave",
      intent: i % 2 === 0 ? "Create" : "Explore",
      emotion: ["Inspired", "Excited", "Determined"][i % 3],
      energy: 100 - i * 10,
      source: "Dashboard"
    });
    
    // 2. Step agentów (integracja 5 wymiarów)
    const a1 = alice.step(90 - i * 8);
    const a2 = bob.step(85 - i * 12);
    
    // 3. Komunikacja sieciowa
    networkSelph.broadcast(alice, a1);
    networkSelph.broadcast(bob, a2);
    
    // 4. Kolektywna inteligencja
    alice.receiveCollectiveIntelligence();
    bob.receiveCollectiveIntelligence();
    
    // 5. Ewolucja w połowie demo
    if (i === 2) {
      pipeline.broadcastUpdate({
        version: "2.1.0",
        identity: "PinkMan-GOK:AI®️🇵🇱 ⚡Enhanced",
        type: "major_evolution"
      });
    }
    
    // 6. Test iteracji ewolucyjnej
    if (i === 3) {
      const iterationResult = pipeline.runIteration(alice.coreSelph);
      console.log("🔄 Evolution iteration result:", iterationResult);
    }
    
    await new Promise(r => setTimeout(r, 150));
  }

  // === FINALNE DASHBOARD STATS ===
  
  console.log("\n🎯 === DASHBOARD MVP SUMMARY ===");
  
  console.log("\n📈 Pipeline Analysis:");
  console.log(pipeline.getPipelineAnalysis());
  
  console.log("\n🤖 Alice System Status:");
  console.log(alice.getSystemStatus());
  
  console.log("\n🤖 Bob System Status:");
  console.log(bob.getSystemStatus());
  
  console.log("\n🌐 Network Analysis:");
  console.log(networkSelph.getNetworkAnalysis());
  
  console.log("\n🧠 Shared Intelligence:");
  console.log(networkSelph.getSharedIntelligence());
  
  console.log("\n📊 Evolution Stats Alice:");
  console.log(alice.getEvolutionStats());
  
  console.log("\n📊 Evolution Stats Bob:");
  console.log(bob.getEvolutionStats());

  // === TEST ZAAWANSOWANYCH FUNKCJI ===
  
  console.log("\n🔧 === ADVANCED FEATURES TEST ===");
  
  // Test direct messaging
  networkSelph.sendDirect(alice, 'bob', { 
    message: "Hey Bob, let's sync consciousness!", 
    type: "direct_sync" 
  });
  
  // Test auto-evolution
  alice.autoEvolve();
  bob.autoEvolve();
  
  // Test system updates
  pipeline.broadcastUpdate({
    mode: "evolutionary",
    filters: { creativity: 1.0, intuition: 0.9 },
    message: "System optimization complete"
  });

  console.log("\n✨ PinkPlayEvo™ Dashboard MVP - Complete!");
  console.log("🎭 All 5 dimensions of consciousness successfully integrated!");
  console.log("🔗 Full pipeline connectivity achieved!");
  console.log("🚀 System ready for production deployment!");
}

main().catch(console.error);
