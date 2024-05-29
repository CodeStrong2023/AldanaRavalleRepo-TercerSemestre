package Clase_5.src.ClaseAbstracta.domain;

public class Rectangulo extends FiguraGeometrica{
    
    //Constructor
    public Rectangulo(String tipoFigura){
        super(tipoFigura);
    }
    
    @Override
    public void dibujar(){ //Implementando el método
        System.out.println("Se imprime un: "+this.getClass().getSimpleName());
    }
}