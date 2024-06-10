package Clase_5.src.Objeto.test;
import Clase_5.src.Objeto.domain.*;


public class TestConversionObjetos{
    public static void main (String[] args) {
        Empleado empleado;
        empleado = new Escritor ("Juan", 5000, TipoEscritura.CLASICO);
        //System.out.printin("empleado =" + empleado);
        //System.out.printin(empleado.obtenerDetalles()); //Si queremos acceder a métodos Escritor
        
        // Downcasting

        // Opcion 1
        //((Escritor)empleado).getTipoEscritura();

        // Opcion2
        Escritor escritor = (Escritor)empleado;
        escritor.getTipoEscritura ();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}