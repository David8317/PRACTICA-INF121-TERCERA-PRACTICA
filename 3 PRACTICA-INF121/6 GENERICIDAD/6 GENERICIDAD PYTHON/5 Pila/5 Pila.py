# TEMA: GENERICIDAD
# Enunciado:
# 5. Crea una clase genérica Pila<T>
# a) Implementa un método para apilar
# b) Implementa un método para desapilar
# c) Prueba la pila con diferentes tipos de datos
# d) Muestra los datos de la pila

class Pila:
    def __init__(self):
        self.elementos = []
# a) 
    def apilar(self, elemento):
        self.elementos.append(elemento)
# b)
    def desapilar(self):
        if self.elementos:
            return self.elementos.pop()
        else:
            return None  
# d) 
    def mostrar(self):
        return self.elementos.copy()

def main():
    # c)

    pila_enteros = Pila()
    pila_enteros.apilar(10)
    pila_enteros.apilar(20)
    pila_enteros.apilar(30)

    print("Pila de enteros:")
    print(pila_enteros.mostrar())

    print("Desapilando:", pila_enteros.desapilar())
    print("Pila de enteros después de desapilar:")
    print(pila_enteros.mostrar())

    pila_cadenas = Pila()
    pila_cadenas.apilar("Hola")
    pila_cadenas.apilar("Mundo")

    print("\nPila de cadenas:")
    print(pila_cadenas.mostrar())

    print("Desapilando:", pila_cadenas.desapilar())
    print("Pila de cadenas después de desapilar:")
    print(pila_cadenas.mostrar())

if __name__ == "__main__":
    main()
