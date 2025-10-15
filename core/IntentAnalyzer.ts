export class IntentAnalyzer {
  analyzeMessage(message: string) {
    // Prosty heurystyczny filtr
    const scamWords = ["scam", "hack", "bitcoin", "transfer", "urgent", "gift"];
    const lower = message.toLowerCase();
    const flagged = scamWords.some(word => lower.includes(word));
    return {
      flagged,
      reason: flagged ? "Suspicious keywords detected" : "Clean"
    };
  }
}
