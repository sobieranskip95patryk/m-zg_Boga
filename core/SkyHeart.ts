
// SkyHeart.ts
// Moduł emocjonalny dla GOK:AI i PinkPlayEvo™

export type EmotionProfile = {
  dominantEmotion: "joy" | "fear" | "anger" | "sadness" | "neutral";
  intensity: number; // 0.0 to 1.0
  contextTags: string[];
};

export type ResponseStyle = {
  tone: "calm" | "playful" | "firm" | "neutral" | "empathetic";
  color: string;
  animation: string;
};

export class SkyHeart {
  userEmotionLog: EmotionProfile[];

  constructor() {
    this.userEmotionLog = [];
  }

  detectEmotion(input: string): EmotionProfile {
    const tone = this.analyzeTone(input);
    const sentiment = this.sentimentAnalysis(input);
    const tempo = this.measureRhythm(input);

    return {
      dominantEmotion: this.classifyEmotion(tone, sentiment),
      intensity: this.calculateIntensity(tone, tempo),
      contextTags: this.extractContext(input)
    };
  }

  modulateResponse(emotion: EmotionProfile): ResponseStyle {
    switch (emotion.dominantEmotion) {
      case "fear":
        return { tone: "calm", color: "#4A90E2", animation: "softPulse" };
      case "joy":
        return { tone: "playful", color: "#F5A623", animation: "bounce" };
      case "anger":
        return { tone: "firm", color: "#D0021B", animation: "shake" };
      case "sadness":
        return { tone: "empathetic", color: "#9013FE", animation: "fade" };
      default:
        return { tone: "neutral", color: "#9B9B9B", animation: "none" };
    }
  }

  expressEmotion(style: ResponseStyle): void {
    this.updateUITheme(style.color, style.animation);
    this.setResponseTone(style.tone);
  }

  reflectOnInteraction(log: EmotionProfile): void {
    this.userEmotionLog.push(log);
    const trends = this.analyzeEmotionTrends();
    this.adaptModulationRules(trends);
  }

  // --- Internal Methods ---

  analyzeTone(text: string): number {
    // Placeholder: NLP tone analysis
    return Math.random();
  }

  sentimentAnalysis(text: string): number {
    // Placeholder: sentiment score
    return Math.random();
  }

  measureRhythm(text: string): number {
    // Placeholder: punctuation + tempo
    return Math.random();
  }

  classifyEmotion(tone: number, sentiment: number): EmotionProfile["dominantEmotion"] {
    if (sentiment > 0.7) return "joy";
    if (sentiment < 0.3 && tone > 0.6) return "anger";
    if (sentiment < 0.3 && tone < 0.4) return "sadness";
    if (tone > 0.8) return "fear";
    return "neutral";
  }

  calculateIntensity(tone: number, tempo: number): number {
    return Math.min(1.0, (tone + tempo) / 2);
  }

  extractContext(text: string): string[] {
    return text.split(" ").filter(word => word.length > 6);
  }

  updateUITheme(color: string, animation: string): void {
    // Connect to frontend theme engine
    console.log(`🎨 Updating UI to ${color} with ${animation}`);
  }

  setResponseTone(tone: string): void {
    console.log(`🗣️ Setting response tone to ${tone}`);
  }

  analyzeEmotionTrends(): EmotionProfile {
    // Basic averaging
    const avgIntensity = this.userEmotionLog.reduce((sum, e) => sum + e.intensity, 0) / this.userEmotionLog.length;
    return {
      dominantEmotion: "neutral",
      intensity: avgIntensity,
      contextTags: []
    };
  }

  adaptModulationRules(trend: EmotionProfile): void {
    console.log("🔁 Adapting modulation rules based on trend:", trend);
  }
}
