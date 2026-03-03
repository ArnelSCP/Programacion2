//para el cronometro
class Cronometro {
    
    private long inicia;
    private long finaliza;

    // nuestro constructor
    public Cronometro() {
        this.inicia = System.currentTimeMillis();
    }

    // metodos para consultar los datos
    public long getInicia() { return inicia; }
    public long getFinaliza() { return finaliza; }

    // reinicia el contador a la hora de este mismo momento
    public void inicia() {
        this.inicia = System.currentTimeMillis();
    }

    // guardamos la hora en que se detuvo
    public void detener() {
        this.finaliza = System.currentTimeMillis();
    }

    // calculamos la resta para saber cuanto tiempo paso
    public long lapsoDeTiempo() {
        return finaliza - inicia;
    }
}
//programa de prueba a parte para que funcione al correrlo
public class Main {
    public static void main(String[] args) throws InterruptedException {

        Cronometro miReloj = new Cronometro();
        System.out.println("Cronometro iniciado.");
        Thread.sleep(2000);
        miReloj.detener();

        System.out.println("Tiempo transcurrido: " + miReloj.lapsoDeTiempo() + " ms");
    }
}

