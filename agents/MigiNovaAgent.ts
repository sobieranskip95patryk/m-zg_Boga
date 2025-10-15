export class MigiNovaAgent {
  id = 'MIGI-NOVA'
  ideas(seed:string){ return [`idea:${seed}:1`, `idea:${seed}:2`, `idea:${seed}:3`] }
}
