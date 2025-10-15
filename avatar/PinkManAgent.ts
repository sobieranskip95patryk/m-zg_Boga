import { AvatarInterface } from './AvatarInterface'
import { ConsciousKernel } from '../system/ConsciousKernel'

export class PinkManAgent implements AvatarInterface {
  kernel: ConsciousKernel
  constructor(){
    this.kernel = new ConsciousKernel()
  }
  perceive(input:number): number {
    return this.kernel.run(input)
  }
  reflect(state:any): string {
    return `PinkMan reflektuje stan: ${JSON.stringify(state)}`
  }
}
