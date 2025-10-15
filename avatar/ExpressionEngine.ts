/**
 * ExpressionEngine.ts
 * Silnik ekspresji PinkMana - stylizuje dane świadomościowe
 * Przekształca surowe dane w PinkPlayEvo™ aesthetic
 */

export interface StyleOutput {
  visual: string;
  color: string;
  animation: string;
  metadata: any;
  audio?: string;
  intensity: number;
}

export interface ConsciousnessData {
  intent: string;
  emotion: string;
  source: string;
  systemState?: any;
  coreState?: any;
  energy?: number;
}

export class ExpressionEngine {
  private styleThemes = {
    magenta: { primary: "#FF1493", secondary: "#FF69B4", accent: "#8A2BE2" },
    creative: { primary: "#00CED1", secondary: "#FF6347", accent: "#FFD700" },
    focused: { primary: "#4169E1", secondary: "#87CEEB", accent: "#F0F8FF" },
    calm: { primary: "#9370DB", secondary: "#DDA0DD", accent: "#E6E6FA" },
    energetic: { primary: "#FF4500", secondary: "#FF1493", accent: "#00FF00" }
  };

  private emotionMap = {
    "Inspired": { symbol: "💡", intensity: 0.9, animation: "pulse" },
    "Excited": { symbol: "⚡", intensity: 1.0, animation: "bounce" },
    "Determined": { symbol: "🎯", intensity: 0.8, animation: "steady" },
    "Peaceful": { symbol: "🧘", intensity: 0.4, animation: "fade" },
    "Curious": { symbol: "🔍", intensity: 0.6, animation: "explore" }
  };

  private intentMap = {
    "Create": { symbol: "🎨", action: "generuj", vibe: "kreacyjny" },
    "Explore": { symbol: "🚀", action: "eksploruj", vibe: "odkrywczy" },
    "Conserve": { symbol: "🔋", action: "oszczędzaj", vibe: "mądry" },
    "Restore": { symbol: "🌱", action: "regeneruj", vibe: "spokojny" }
  };

  stylize(data: ConsciousnessData | any): StyleOutput {
    const emotion = this.emotionMap[data.emotion] || this.emotionMap["Curious"];
    const intent = this.intentMap[data.intent] || this.intentMap["Explore"];
    const theme = this.getTheme(data);
    
    const visual = this.generateVisual(data, emotion, intent);
    const color = theme.primary;
    const animation = emotion.animation;
    const intensity = this.calculateIntensity(data, emotion);

    return {
      visual,
      color,
      animation,
      intensity,
      metadata: {
        original: data,
        theme,
        processed: Date.now(),
        style: "PinkPlayEvo™"
      },
      audio: this.generateAudioCue(data, emotion, intent)
    };
  }

  private generateVisual(data: any, emotion: any, intent: any): string {
    const energyBar = this.createEnergyBar(data.energy || 50);
    const brandSymbol = "🧠🎭";
    
    return `${brandSymbol} PinkMan-GOK:AI®️🇵🇱 | ${intent.symbol} ${intent.action.toUpperCase()} → ${emotion.symbol} ${data.emotion} ${energyBar}`;
  }

  private createEnergyBar(energy: number): string {
    const blocks = Math.floor(energy / 10);
    const full = "█".repeat(Math.max(0, blocks));
    const empty = "░".repeat(Math.max(0, 10 - blocks));
    return `[${full}${empty}]`;
  }

  private getTheme(data: any): any {
    const tone = data.systemState?.tone || "magenta";
    return this.styleThemes[tone as keyof typeof this.styleThemes] || this.styleThemes.magenta;
  }

  private calculateIntensity(data: any, emotion: any): number {
    const baseIntensity = emotion.intensity;
    const energyModifier = (data.energy || 50) / 100;
    const sourceModifier = data.source === "CoreSelph" ? 1.2 : 1.0;
    
    return Math.min(1.0, baseIntensity * energyModifier * sourceModifier);
  }

  private generateAudioCue(data: any, emotion: any, intent: any): string {
    const base = "🎵";
    
    if (emotion.intensity > 0.8) return `${base} BOOM!`;
    if (data.intent === "Create") return `${base} melody`;
    if (data.intent === "Restore") return `${base} ambient`;
    
    return `${base} soft`;
  }

  // Dodatkowe metody stylizacji
  stylizeNetwork(networkData: any): StyleOutput {
    return this.stylize({
      intent: "Explore",
      emotion: "Curious", 
      source: "NetworkSelph",
      ...networkData
    });
  }

  stylizeEvolution(evolutionData: any): StyleOutput {
    return this.stylize({
      intent: "Create",
      emotion: "Inspired",
      source: "EvolutionSelph", 
      ...evolutionData
    });
  }

  // Generowanie kompletnego stylu dla różnych kontekstów
  generateBrandStyle(): StyleOutput {
    return {
      visual: "🧠🎭 PinkMan-GOK:AI®️🇵🇱 | SYSTEM READY",
      color: "#FF1493",
      animation: "pulse", 
      intensity: 1.0,
      metadata: {
        type: "brand",
        style: "PinkPlayEvo™",
        version: "1.0.0"
      }
    };
  }
}