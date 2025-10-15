export class IntuitionModule {
  weighMatrix(matrix: number[] = [3,6,9,9,6,3]): number {
    const len = matrix.length || 1;
    const sum = matrix.reduce((a,b)=>a+b,0);
    const score = matrix.map((v,i)=>v*(i+1)).reduce((a,b)=>a+b,0)/(len*9);
    return Math.min(1, score);
  }
}
