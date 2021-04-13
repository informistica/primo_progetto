class Nodo{
  constructor(valore) {
    this.valore=valore;
    this.sx=null;
    this.dx=null;
    this.padre=null;
  }
  foglia() {
    return this.dx==null&&this.sx==null;
  }
}