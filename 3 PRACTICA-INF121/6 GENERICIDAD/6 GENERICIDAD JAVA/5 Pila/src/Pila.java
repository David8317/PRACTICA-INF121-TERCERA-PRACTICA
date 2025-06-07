// TEMA: GENERICIDAD
// Enunciado:
// 5. Crea una clase genérica Pila<T>
// a) Implementa un método para apilar
// b) Implementa un método para desapilar
// c) Prueba la pila con diferentes tipos de datos
// d) Muestra los datos de la pila

import java.util.ArrayList;
import java.util.List;

class Pila<T> {
    private List<T> elementos;

    public Pila() {
        elementos = new ArrayList<>();
    }

    // a) 
    public void apilar(T elemento) {
        elementos.add(elemento);
    }

    // b)
    public T desapilar() {
        if (elementos.isEmpty()) {
            return null; 
        }
        return elementos.remove(elementos.size() - 1);
    }
    // d) 
    public List<T> mostrar() {
        return new ArrayList<>(elementos); 
    }
}
