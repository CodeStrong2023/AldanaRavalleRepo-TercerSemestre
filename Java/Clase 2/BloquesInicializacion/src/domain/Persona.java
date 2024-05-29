package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ // Bloque de inicializacion estatico
        System.out.println("Ejecución del bloque estático.");
        ++Persona.contadorPersonas;
    }

    {// Bloque de codigo no estatico (Contexto dinamico)
        System.out.println("Ejecucion del bloque NO estatico");
        this.idPersona = Persona.contadorPersonas++; // Incrementar el atributo
    }

    public Persona(){
        System.out.println("Ejecucion de constructor");
    }

    public int getidPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona [idPersona=" + idPersona + "]";
    }

    
}
