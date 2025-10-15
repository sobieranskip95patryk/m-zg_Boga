/**
 * quickTest.ts
 * Szybki test systemu PinkPlayEvo™ Jaźń
 */
import { PinkManAgent } from './avatar/PinkManAgent';
import { NetworkSelph } from './network/NetworkSelph';
import { EvolutionaryPipeline } from './pipeline/EvolutionaryPipeline';

// Quick test
console.log("🧪 Quick Test Start...");

const network = new NetworkSelph();
const agent = new PinkManAgent('test', network);
const pipeline = new EvolutionaryPipeline([agent, agent.coreSelph]);

// Test pipeline transmission
pipeline.transmit({
  intent: "Test",
  emotion: "Curious",
  energy: 80
});

// Test evolution
agent.evolve("PinkMan-GOK:AI®️🇵🇱 Test");

// Test external connections
agent.connectToGOKAI();

console.log("✅ Quick Test Complete!");
console.log("System Status:", agent.getSystemStatus());