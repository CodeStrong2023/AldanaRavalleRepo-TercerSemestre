package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTRC = 10;

    // El metodo insertar es abstracto y sin cuermo

    void insertar();
    void listar();
    void actualizar();
    void eliminar();
}