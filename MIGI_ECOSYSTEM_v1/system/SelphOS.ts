import { CoreSelph } from '../core/CoreSelph'
import { IntuitionModule } from '../core/IntuitionModule'

export class SelphOS {
  core: CoreSelph
  intuition: IntuitionModule
  constructor() {
    this.core = new CoreSelph()
    this.intuition = new IntuitionModule()
  }
  evaluate(x:number, a=1, b=0, fib=8, matrix:number[]=[3,6,9,9,6,3]) {
    const ninePi = 9*Math.PI
    const fibo = (k:number):number => k<=1 ? k : fibo(k-1)+fibo(k-2)
    const raw = ninePi + fibo(fib) + fibo(fib-1) + (a*x + b)
    const m = this.intuition.weighMatrix(matrix)
    const k = 1 + 0.5*m
    const ps = 100/(1 + Math.exp(-k*(raw/100)))
    return Math.max(0, Math.min(100, ps))
  }
}
