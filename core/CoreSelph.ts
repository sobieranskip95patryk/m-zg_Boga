export class CoreSelph {
  constructor(public id: string = 'CoreSelph-0') {}

  signature(n: number = 8): number {
    // S(GOK:AI) ≈ 9π + F(n) + F(n-1)
    const ninePi = 9 * Math.PI;
    const fib = (k:number):number => k<=1 ? k : fib(k-1)+fib(k-2);
    const v = ninePi + fib(n) + fib(n-1);
    return v;
  }
}
