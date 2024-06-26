package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributo Privado";

    private Clase4() {
        System.out.println("Constructor privado");

    }

    // Constructor public para poder crear objetos
    public Clase4(String argumento){ // Se llama al constructor vacio
        this();
        System.out.println("Constructor publico");
    }

    // Metodo private
    private void metodoPrivado(){
        System.out.println("Método privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }

    
}
