
package test;
import enumeracion.Continentes;
//import enumeracion.Dias;

public class TestEnumeracion {
    public static void main(String[] args) {
        //System.out.println("Día 1: "+Dias.LUNES);
        //indicarDiaSemana(Dias.LUNES);
        System.out.println("Continente No. 1: "+Continentes.AFRICA);
        System.out.println("No. de paises en el continente: "+ Continentes.AFRICA.getPaises());
        System.out.println("No. de habitantes en el continente: "+ Continentes.AFRICA.getHabitantes());

        System.out.println("Continente No. 2: "+Continentes.EUROPA);
        System.out.println("No. de paises en el continente: "+ Continentes.EUROPA.getPaises());
        System.out.println("No. de habitantes en el continente: "+ Continentes.EUROPA.getHabitantes());

        System.out.println("Continente No. 3: "+Continentes.ASIA);
        System.out.println("No. de paises en el continente: "+ Continentes.ASIA.getPaises());
        System.out.println("No. de habitantes en el continente: "+ Continentes.ASIA.getHabitantes());

        System.out.println("Continente No. 4: "+Continentes.AMERICA);
        System.out.println("No. de paises en el continente: "+ Continentes.AMERICA.getPaises());
        System.out.println("No. de habitantes en el continente: "+ Continentes.AMERICA.getHabitantes());

        System.out.println("Continente No. 5: "+Continentes.OCEANIA);
        System.out.println("No. de paises en el continente: "+ Continentes.OCEANIA.getPaises());
        System.out.println("No. de habitantes en el continente: "+ Continentes.OCEANIA.getHabitantes());

    }
    
    /*private static void indicarDiaSemana(Dias dias){
        switch (dias) {
            case LUNES:
                System.out.println("Primer día de la semana.");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana.");
                break;
            case MIERCOLES:
                System.out.println("Tercer día de la semana.");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana.");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana.");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana.");
                break;
            case DOMINGO:
                System.out.println("Septimo día de la semana.");
                break;
            default:
                System.out.println("Informacion incorrecta");
                break;
        }
    }*/
}
