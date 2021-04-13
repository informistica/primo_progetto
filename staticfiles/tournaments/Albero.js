class Albero {
  constructor() {
    this.strati = [
      [],
    ];
    this.radice = null;
  }

  risultato() {
    this.risultato2(this.radice);
  }
  risultato2(nodo) {
    if (nodo == null)
      return;
    if (nodo.sx.foglia()) {
      document.write(nodo.sx.valore.nome);
      document.write(" vs ");
      document.write(nodo.dx.valore.nome);
      document.write("=>" + nodo.valore.nome + "<br>");
      return;
    }
    this.risultato2(nodo.sx);
    this.risultato2(nodo.dx);
  }
  generaInfoGrafico() {
    const desc= "Forza: "+this.radice.valore.forza;
    const name = {
      val: this.radice.valore.nome,
    };
    const children = [];
    if (this.radice.sx != null)
      this.generaInfoGrafico2(this.radice.sx, children);
    if (this.radice.dx != null)
      this.generaInfoGrafico2(this.radice.dx, children);
    return {text:{name,desc},children};
  }
  generaInfoGrafico2(nodo, vettore) {
    if (nodo.foglia()) {
      vettore.push({
        text: {
          name:nodo.valore.nome,
          desc:"Forza: "+nodo.valore.forza,
        },
      });
      return;
    }
    const children = [];
    if (nodo.sx != null) 
      this.generaInfoGrafico2(nodo.sx, children);
    
    if (nodo.dx != null) 
      this.generaInfoGrafico2(nodo.dx, children);
    
    vettore.push({
      text:{
        name: nodo.valore.nome,
        desc: "Forza: "+nodo.valore.forza,
      },
      children,
    });
  }
}