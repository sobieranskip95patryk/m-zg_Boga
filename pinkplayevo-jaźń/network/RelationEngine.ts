/**
 * RelationEngine.ts
 * Silnik relacji - liczy siłę więzi między agentami na podstawie interakcji.
 */
export type Relation = { a: string; b: string; weight: number };

export class RelationEngine {
  relations: Relation[] = [];

  strengthen(a: string, b: string, amount = 0.1) {
    let r = this.relations.find(x => (x.a===a && x.b===b) || (x.a===b && x.b===a));
    if (!r) {
      r = { a, b, weight: 0 };
      this.relations.push(r);
    }
    r.weight = Math.min(1, r.weight + amount);
  }

  getRelation(a: string, b: string) {
    return this.relations.find(x => (x.a===a && x.b===b) || (x.a===b && x.b===a)) || { a, b, weight: 0 };
  }
}
