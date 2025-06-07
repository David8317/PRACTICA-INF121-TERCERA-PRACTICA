import java.util.List;

public class Main {
    public static void main(String[] args) {
        // b) Prueba el catálogo con libros
        Catalogo<Libro> catalogoLibros = new Catalogo<>();
        Libro libro1 = new Libro("1984", "George Orwell");
        Libro libro2 = new Libro("El principito", "Antoine de Saint-Exupéry");
        catalogoLibros.agregar(libro1);
        catalogoLibros.agregar(libro2);

        System.out.println("Catálogo de libros:");
        System.out.println(catalogoLibros.obtenerTodos());

        List<Libro> encontrados = catalogoLibros.buscar(libro1);
        System.out.println("Buscando libro '1984' de George Orwell:");
        System.out.println(encontrados);

        // c) Prueba el catálogo con productos
        Catalogo<Producto> catalogoProductos = new Catalogo<>();
        Producto prod1 = new Producto("Laptop", 1500);
        Producto prod2 = new Producto("Teléfono", 800);
        Producto prod3 = new Producto("Monitor", 300);
        catalogoProductos.agregar(prod1);
        catalogoProductos.agregar(prod2);
        catalogoProductos.agregar(prod3);

        System.out.println("\nCatálogo de productos:");
        System.out.println(catalogoProductos.obtenerTodos());

        List<Producto> encontradosProd = catalogoProductos.buscar(prod2);
        System.out.println("Buscando producto 'Teléfono' de precio 800:");
        System.out.println(encontradosProd);
    }
}
