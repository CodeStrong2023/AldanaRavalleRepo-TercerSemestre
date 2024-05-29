package test;

import domain.Persona;

public class TestForEach {
    public static void main(String[] args) {

        int edades[] = { 5, 6, 8, 9 }; // sintaxis resumida

        // for (int i = 0; i < edades.length; i++);
        for (int edad : edades) {
            System.out.println("Edad: " + edad);
        }
        // No tiene contador, por lo que no tiene indice

        Persona personas[] = { new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz") };
        // No utilizar var en los arreglos, utilizar el tipo de dato especifico

        // ForEach
        for(Persona persona: personas){
            System.out.println("persona: "+persona);
        }
    }
}
