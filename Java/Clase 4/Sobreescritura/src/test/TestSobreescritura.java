package test;
import domain.*;

public class TestSobreescritura {
    public static void main(String[] args) {
        Empleado empleado = new Empleado("Maria", 10000);
        imprimir(empleado);
        //System.out.println("empleado1: "+ empleado1.obtenerDetalles());

        empleado = new Gerente("Jose", 5000, "Sistemas");
        imprimir(empleado);
        //System.out.println("gerente1: "+ gerente1.obtenerDetalles());
    }

    public static void imprimir(Empleado empleado){
        String detalles = empleado.obtenerDetalles();
        System.out.println("empleado: "+ detalles);
    }   
}