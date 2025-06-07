# TEMA: GENERICIDAD
# Enunciado:
# 3. Crea una clase genérica Catalogo<T> que almacene productos o libros.
# a) Agrega métodos para agregar y buscar elemento
# b) Prueba el catálogo con libros
# c) Prueba el catálogo con productos

class Catalogo:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def buscar(self, opjeto):
        resultados = []
        for elem in self.elementos:
            if callable(opjeto):
                if opjeto(elem):
                    resultados.append(elem)
            else:
                if elem == opjeto:
                    resultados.append(elem)
        return resultados
    
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}')"

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return f"Producto(nombre='{self.nombre}', precio={self.precio})"

def main():
    # b) Prueba el catálogo con libros
    catalogo_libros = Catalogo()
    catalogo_libros.agregar(Libro("1984", "George Orwell"))
    catalogo_libros.agregar(Libro("El principito", "Antoine de Saint-Exupéry"))

    print("Catálogo de libros:")
    print(catalogo_libros.elementos)

    libros_orwell = catalogo_libros.buscar(lambda libro: libro.autor == "George Orwell")
    print("Libros de George Orwell:")
    print(libros_orwell)

    # c) Prueba el catálogo con productos
    catalogo_productos = Catalogo()
    catalogo_productos.agregar(Producto("Laptop", 1500))
    catalogo_productos.agregar(Producto("Teléfono", 800))
    catalogo_productos.agregar(Producto("Monitor", 300))

    print("\nCatálogo de productos:")
    print(catalogo_productos.elementos)
    
    productos_telefono = catalogo_productos.buscar(lambda p: p.nombre == "Teléfono")
    print("Productos con nombre 'Teléfono':")
    print(productos_telefono)

if __name__ == "__main__":
    main()
