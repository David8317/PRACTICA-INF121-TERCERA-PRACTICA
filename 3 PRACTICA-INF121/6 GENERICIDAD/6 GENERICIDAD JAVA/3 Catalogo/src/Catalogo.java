// TEMA: GENERICIDAD
// Enunciado:
// 3. Crea una clase genérica Catalogo<T> que almacene productos o libros.
// a) Agrega métodos para agregar y buscar elemento
// b) Prueba el catálogo con libros
// c) Prueba el catálogo con productos

import java.util.ArrayList;
import java.util.List;

public class Catalogo<T> {
    private List<T> elementos;

    public Catalogo() {
        this.elementos = new ArrayList<>();
    }
    public void agregar(T elemento) {
        elementos.add(elemento);
    }
    public List<T> buscar(T objeto) {
        List<T> resultados = new ArrayList<>();
        for (T elem : elementos) {
            if (elem.equals(objeto)) {
                resultados.add(elem);
            }
        }
        return resultados;
    }
    public List<T> obtenerTodos() {
        return elementos;
    }
}
