package test;
import domain.*;

public class TestInstanceOf {
    public static void main(String[] args) {
        Empleado empleado = new Empleado("Maria", 10000);
        determinarTipo(empleado);
        empleado = new Gerente("Jose", 5000, "Sistemas");
        determinarTipo(empleado);
    }

    public static void determinarTipo(Empleado empleado){
        if(empleado instanceof Gerente){
            System.out.println("Es de tipo Gerente");
            // Gerente gerente = (Gerente)empleado;
            // System.out.println("gerente: "+gerente.getDepartamento());

        }
        else if(empleado instanceof Empleado){
            System.out.println("Es de tipo Empleado");
            // Gerente gerente = (Gerente)empleado;
            // System.out.println("gerente: "+gerente.getDepartamento());

        }
        else if(empleado instanceof Object){
            System.out.println("Es de tipo Object");
        }
    }   
}