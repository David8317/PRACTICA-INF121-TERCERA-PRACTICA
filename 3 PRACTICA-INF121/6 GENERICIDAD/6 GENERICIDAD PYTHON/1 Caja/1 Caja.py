# TEMA: GENERICIDAD
# Enunciado:
# 1. Crea una clase genérica Caja<T> para guardar algún tipo de objeto.
#
# Incisos:
# a) Agrega métodos guardar() y obtener().
# b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo.
# c) Muestra el contenido de las cajas.

class Caja:
    def __init__(self):
        self.contenido = []  

    def guardar(self, dato):
        self.contenido.append(dato)  

    def obtener(self):
        return self.contenido
# b) 
def main():
    caja_enteros = Caja()
    caja_enteros.guardar(12)
    caja_enteros.guardar(8)
    caja_enteros.guardar(20)
    print("Contenido de caja_enteros:", caja_enteros.obtener())

    caja_cadenas = Caja()
    caja_cadenas.guardar("hola")
    caja_cadenas.guardar("mundo")
    print("Contenido de caja_cadenas:", caja_cadenas.obtener())

if __name__ == "__main__":
    main()