export class MigiCoreAgent {
  id = 'MIGI-CORE'
  handle(payload: any){ return { id:this.id, ok:true, payload } }
}
