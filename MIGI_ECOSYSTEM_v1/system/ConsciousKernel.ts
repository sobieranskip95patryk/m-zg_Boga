import { SelphOS } from './SelphOS'

export class ConsciousKernel {
  os: SelphOS
  constructor(){
    this.os = new SelphOS()
  }
  run(input:number){
    return this.os.evaluate(input)
  }
}
