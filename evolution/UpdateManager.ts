/**
 * UpdateManager.ts
 * Harmonogram aktualizacji i migracji stanu między wersjami.
 */
import { CoreSelph } from "../core/CoreSelph";

export class UpdateManager {
  history: { version: string; snapshot: any }[] = [];

  snapshot(core: CoreSelph, version = 'v0') {
    const s = { version, state: core.getSnapshot(), ts: Date.now() };
    this.history.push(s);
    return s;
  }

  migrate(core: CoreSelph, data: any) {
    // prosta migracja: dopasuj brakujące pola
    core.state = { ...core.state, ...data.state };
  }
}
