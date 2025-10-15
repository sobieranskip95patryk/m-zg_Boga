/**
 * ConsciousKernel.ts
 * Lekka reprezentacja rdzenia świadomego - agreguje informacje i publikuje intencję.
 */
import { SelphOS } from "./SelphOS";

export class ConsciousKernel {
  os: SelphOS;

  constructor(os: SelphOS) {
    this.os = os;
  }

  publishIntent() {
    const snap = this.os.snapshot();
    const intent = snap.decision ? snap.decision.name : 'observe';
    return { intent, meta: snap.core };
  }
}
