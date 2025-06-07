import pickle
import os

class Cliente:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Cliente(id={self.id}, nombre='{self.nombre}', telefono={self.telefono})"


class ArchivoCliente:
    def __init__(self, nombre_archivo):
        self.nomA = nombre_archivo

    def crear_archivo(self):
        with open(self.nomA, 'wb') as f:
            pass  
        print(f"Archivo creado: {self.nomA}")

    def guarda_cliente(self, cliente):
        modo = 'ab' if os.path.exists(self.nomA) else 'wb'
        with open(self.nomA, modo) as f:
            pickle.dump(cliente, f)

    def buscar_cliente(self, id_buscar):
        try:
            with open(self.nomA, 'rb') as f:
                while True:
                    try:
                        cliente = pickle.load(f)
                        if cliente.id == id_buscar:
                            return cliente
                    except EOFError:
                        break
        except (FileNotFoundError, IOError):
            print("Archivo no encontrado o error de lectura.")
        return None

    def buscar_celular_cliente(self, id_buscar):
        cliente = self.buscar_cliente(id_buscar)
        return cliente  

if __name__ == "__main__":
    arch = ArchivoCliente("clientes.dat")

    arch.crear_archivo()
    arch.guarda_cliente(Cliente(1, "Ana", 67890123))
    arch.guarda_cliente(Cliente(2, "Luis", 76543210))
    arch.guarda_cliente(Cliente(3, "Pedro", 71234567))
    # Buscar cliente por ID
    c1 = arch.buscar_cliente(2)
    if c1:
        print("Cliente encontrado por ID:", c1)
    else:
        print("Cliente no encontrado.")
    # Buscar cliente y mostrar celular
    c2 = arch.buscar_celular_cliente(3)
    if c2:
        print(f"Cliente con celular: {c2.nombre}, Teléfono: {c2.telefono}")
    else:
        print("Cliente no encontrado.")
