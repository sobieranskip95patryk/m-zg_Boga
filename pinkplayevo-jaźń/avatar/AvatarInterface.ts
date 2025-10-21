/**
 * AvatarInterface.ts
 * Interfejs komunikacji między systemem a zewnętrznym światem (UI, sieć).
 */
import { PinkManAgent } from "./PinkManAgent";

export interface IAvatarAdapter {
  render(agent: PinkManAgent): Promise<void>;
  sendAction(agent: PinkManAgent, action: string): Promise<void>;
}

export class ConsoleAvatarAdapter implements IAvatarAdapter {
  async render(agent: PinkManAgent) {
    console.log('Avatar render:', agent.name, agent.os.snapshot());
  }
  async sendAction(agent: PinkManAgent, action: string) {
    console.log('Action from avatar:', action);
  }
}
