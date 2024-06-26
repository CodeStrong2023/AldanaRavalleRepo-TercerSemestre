import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        List<Persona> personas = new ArrayList<>();

        // Empezar con el menu
        var salir = false;
        while (!salir) {
            mostrarMenu();

            try {
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e) {
                System.out.println("Ocurrió un error: " + e.getMessage());
            }

            System.out.println();
        } // Fin del ciclo while
    } // Fin del main

    private static void mostrarMenu() {
        // mostramos las opciones
        System.out.print("""
                ******* Listado de Personas *******
                1. Agregar
                2. Listar
                3. Salir
                """);
        System.out.print("Ingrese una de las opciones: ");
    } // Fin de mostrarMenu

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas) {
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        // Revisamos la opcion digita a través de un switch
        switch (opcion) {
            case 1 -> {// Agrear una persona a la lista
                System.out.print("Ingrese el nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Ingrese el telefono: ");
                var tel = entrada.nextLine();
                System.out.print("Ingrese el correo: ");

                // Crear objeto persona
                var email = entrada.nextLine();
                var persona = new Persona(nombre, tel, email);
                personas.add(persona);
                System.out.println("La lista tiene " + personas.size() + " elementos");
            }
            case 2 -> {// Listar a las personas
                System.out.println("Listado de personas: ");
                // Mejonas con lambda y el método de referencia
                // personas.forEach((persona) -> System.out.println(persona));
                personas.forEach(System.out::println);
            }
            case 3 -> {
                System.out.println("¡Hasta pronto!");
                salir = true;
            }
            default -> System.out.println("Opcion incorrecta: " + opcion);
        } // Fin del switch
        return salir;

    } // fin del método ejecutarOperacion
} // Fin de la clase ListadoPersonasApp
