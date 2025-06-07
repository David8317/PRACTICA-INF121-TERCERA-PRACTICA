import java.util.ArrayList;

public class Caja<T> {
    private ArrayList<T> contenido;

    public Caja() {
        contenido = new ArrayList<T>();
    }

    public void guardar(T dato) {
        contenido.add(dato);
    }

    public ArrayList<T> obtener() {
        return contenido;
    }
}

