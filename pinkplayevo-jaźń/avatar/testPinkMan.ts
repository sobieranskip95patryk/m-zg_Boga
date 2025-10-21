/**
 * testPinkMan.ts
 * Test PinkMana zgodnie z instrukcją z Części 2.3
 */

import { PinkManAgent } from "./PinkManAgent";
import { NetworkSelph } from "../network/NetworkSelph";

console.log("🧪 Testing PinkMan Agent...");

// Test podstawowy
const network = new NetworkSelph();
const pinkMan = new PinkManAgent("test_agent", network);

// Test receiveConsciousnessData
pinkMan.receiveConsciousnessData({
  intent: "Create",
  emotion: "Inspired",
  source: "EvolutionSelph"
});

// Test ewolucji
pinkMan.evolve("PinkMan_TestVersion_1.0");
pinkMan.updateAvatarVersion("2.0.0");
pinkMan.syncWithEvolution();

// Test komunikacji sieciowej
pinkMan.connectToGOKAI();

console.log("✅ PinkMan test completed!");
console.log("Status:", pinkMan.getSystemStatus());