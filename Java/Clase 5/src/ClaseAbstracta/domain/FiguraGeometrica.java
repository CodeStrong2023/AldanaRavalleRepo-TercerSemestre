package Clase_5.src.ClaseAbstracta.domain;

public abstract class FiguraGeometrica {
    protected String tipoFigura;
    
    protected FiguraGeometrica (String tipoFigura) {
        this.tipoFigura = tipoFigura;
    }
    
    //Método abstracto
    public abstract void dibujar();

    //Agregar get y set
    public String getTipoFigura() {
        return tipoFigura;
    }

    public void setTipoFigura(String tipoFigura) {
        this.tipoFigura = tipoFigura;
    }

    @Override
    public String toString() {
        return "FiguraGeometrica [tipoFigura=" + tipoFigura + "]";
    }
}