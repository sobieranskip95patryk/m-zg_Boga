/**
 * IntuitionModule.ts
 * Lekki moduł heurystyczny - prosty silnik podejmowania decyzji oparty na regułach.
 */
export type Signal = { name: string; strength: number };

export class IntuitionModule {
  private memory: Signal[] = [];

  registerSignal(s: Signal) {
    this.memory.push(s);
    // utrzymujemy krótką pamięć
    if (this.memory.length > 50) this.memory.shift();
  }

  decide(): Signal | null {
    if (this.memory.length === 0) return null;
    // wybierz najsilniejszy sygnał
    return this.memory.reduce((a, b) => (a.strength >= b.strength ? a : b));
  }
}
