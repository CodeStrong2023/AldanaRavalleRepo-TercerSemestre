package test;

public class TestAutoboxinUnboxing {
    public static void main(String[] args) {
        
        // Clases envolventas o Wrapper

        int enteroPrim = 10;
        System.out.println("enteroPrim: "+ enteroPrim); // Es un numero
        
        // Esto es Autoboxing
        Integer entero = 10;
        System.out.println("entero: " + entero.toString()); // Es una cadena
        System.out.println("entero: " + entero.shortValue()); // Es un short
        System.out.println("entero: " + entero.intValue()); // Es un int
        System.out.println("entero: " + entero.doubleValue()); // Es un double

        // Esto es Unboxing
        int entero2 = entero;
        System.out.println("entero2: "+ entero2);
    }
}
