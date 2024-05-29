package enumeracion;

public enum Continentes {
    AFRICA(53,"1.2 Billones"),
    EUROPA(46, "1.1 Billones"),
    ASIA(44, "1.9 Billones"),
    AMERICA(34, "150 Billones"),
    OCEANIA(14, "1.2 Billones");

    private final int paises;
    private String habitantes;
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
     }

     // Metodos get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
}
