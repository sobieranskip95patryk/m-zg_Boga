/**
 * InterfaceLayer.ts
 * Warstwa interfejsu PinkMana - renderuje stylizowane dane w UI
 * Może być podpięta pod React, Vue, Flutter, Unity, Terminal
 */

export interface RenderOutput {
  visual: string;
  color: string;
  animation: string;
  intensity: number;
  metadata: any;
  audio?: string;
  timestamp?: number;
}

export class InterfaceLayer {
  private renderHistory: RenderOutput[] = [];
  private maxHistory = 100;

  render(styledOutput: RenderOutput) {
    // Zapisz w historii
    this.renderHistory.push({
      ...styledOutput,
      timestamp: Date.now()
    });
    
    // Utrzymuj historię w rozsądnych rozmiarach
    if (this.renderHistory.length > this.maxHistory) {
      this.renderHistory.shift();
    }

    // Renderuj w konsoli z kolorami i animacją
    this.renderToConsole(styledOutput);
    
    // Tu można dodać inne metody renderowania:
    // this.renderToWeb(styledOutput);
    // this.renderToMobile(styledOutput);
    // this.renderToVR(styledOutput);
  }

  private renderToConsole(output: RenderOutput) {
    const intensityBar = "▓".repeat(Math.floor(output.intensity * 10));
    const audioIcon = output.audio ? `${output.audio}` : "";
    
    console.log(`
🧠🎭 PinkMan Interface Layer:
${output.visual}
Color: ${output.color} | Animation: ${output.animation} | Intensity: [${intensityBar}] ${audioIcon}
---
    `);
  }

  // API do pobierania historii renderowania
  getRenderHistory(): RenderOutput[] {
    return [...this.renderHistory];
  }

  getLastRender(): RenderOutput | null {
    return this.renderHistory.length > 0 ? this.renderHistory[this.renderHistory.length - 1] : null;
  }

  // Metody przygotowane pod różne platformy
  renderToWeb(output: RenderOutput) {
    // Tu podpiąć React/Vue komponenty
    // document.getElementById('pinkman-ui').innerHTML = output.visual;
    console.log("📱 Web render:", output.visual);
  }

  renderToMobile(output: RenderOutput) {
    // Tu podpiąć Flutter/React Native
    console.log("📱 Mobile render:", output.visual);
  }

  renderToVR(output: RenderOutput) {
    // Tu podpiąć Unity/A-Frame
    console.log("🥽 VR render:", output.visual);
  }

  // Metody kontrolne interfejsu
  clear() {
    this.renderHistory = [];
    console.clear();
  }

  setMaxHistory(max: number) {
    this.maxHistory = max;
  }
}