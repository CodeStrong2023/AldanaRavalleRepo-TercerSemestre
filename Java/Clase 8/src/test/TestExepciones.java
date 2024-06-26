package test;

import static aritmetica.Aritmetica.division;

import excepciones.OperacionExcepcion;

public class TestExepciones {
    public static void main(String[] args) {
        int resultado = 0;
        try {
            resultado = division(10, 0);
        } catch (OperacionExcepcion e) {
            System.out.println("Ocurrio un error del tipo OperacionExepcion");
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println("Ocurrio un error");
            e.printStackTrace(System.out);
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Se reviso la division");
        }
        System.out.println("La variable resultado vale: " + resultado);
    }
}
