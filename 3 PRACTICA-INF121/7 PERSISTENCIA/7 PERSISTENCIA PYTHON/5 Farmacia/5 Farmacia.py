import pickle
import os

class Medicamento:
    def __init__(self):
        self.nombre = ""
        self.codMedicamento = 0
        self.tipo = ""
        self.precio = 0.0

    def cargar(self, nombre, cod, tipo, precio):
        self.nombre = nombre
        self.codMedicamento = cod
        self.tipo = tipo
        self.precio = precio

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Código: {self.codMedicamento}, Tipo: {self.tipo}, Precio: {self.precio}")

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio

    def getNombre(self):
        return self.nombre


class Farmacia:
    def __init__(self):
        self.nombreFarmacia = ""
        self.sucursal = 0
        self.direccion = ""
        self.medicamentos = []

    def cargar(self, nombreFarmacia, sucursal, direccion, lista_medicamentos):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = lista_medicamentos

    def mostrar(self):
        print(f"\nFarmacia: {self.nombreFarmacia}, Sucursal: {self.sucursal}, Dirección: {self.direccion}")
        for med in self.medicamentos:
            med.mostrar()

    def getDireccion(self):
        return self.direccion

    def getSucursal(self):
        return self.sucursal

    def mostrarMedicamentos(self, tipo):
        for med in self.medicamentos:
            if med.getTipo().lower() == tipo.lower():
                med.mostrar()

    def buscaMedicamento(self, nombreMedicamento):
        for med in self.medicamentos:
            if med.getNombre().lower() == nombreMedicamento.lower():
                return True
        return False


class ArchFarmacia:
    def __init__(self, nombre_archivo):
        self.na = nombre_archivo

    def crearArchivoConDatos(self):
        #  medicamentos farmacia 1
        m1 = Medicamento()
        m1.cargar("Paracetamol", 101, "resfrio", 12.5)
        m2 = Medicamento()
        m2.cargar("Golpex", 102, "analgesico", 18.0)
        m3 = Medicamento()
        m3.cargar("Ibuprofeno", 103, "tos", 15.5)
        m4 = Medicamento()
        m4.cargar("Ambroxol Jarabe", 202, "tos",  18.0)
        f1 = Farmacia()
        f1.cargar("Farmacop", 1, "Av. Achocalla #100", [m1, m2, m3, m4])

        #  medicamentos farmacia 2
        m5 = Medicamento()
        m5.cargar("Tosilax", 104, "tos", 25.0)
        m6 = Medicamento()
        m6.cargar("Panadol", 105, "resfrio", 10.0)
        f2 = Farmacia()
        f2.cargar("Farmacia Vida", 2, "Calle Quime #200", [m5, m6])

        with open(self.na, 'wb') as f:
            lista_farmacias = [f1, f2]
            pickle.dump(lista_farmacias, f)

    def listar(self):
        try:
            with open(self.na, 'rb') as f:
                print("Listado de farmacias:")
                lista_farmacias = pickle.load(f)
                for farmacia in lista_farmacias:
                    farmacia.mostrar()
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def mostrarMedicamentosTosSucursal(self, sucursalX):
        try:
            with open(self.na, 'rb') as f:
                lista_farmacias = pickle.load(f)
                for farmacia in lista_farmacias:
                    if farmacia.getSucursal() == sucursalX:
                        print(f"\nSucursal {sucursalX} - Medicamentos tipo 'tos':")
                        farmacia.mostrarMedicamentos("tos")
        except:
            print("Error leyendo archivo.")

    def mostrarSucursalesConMedicamento(self, nombre_med):
        try:
            with open(self.na, 'rb') as f:
                lista_farmacias = pickle.load(f)
                print(f"\nSucursales que tienen el medicamento '{nombre_med}':")
                for farmacia in lista_farmacias:
                    if farmacia.buscaMedicamento(nombre_med):
                        print(f"Sucursal: {farmacia.getSucursal()}, Dirección: {farmacia.getDireccion()}")
        except:
            print("Error leyendo archivo.")


if __name__ == "__main__":
    arch = ArchFarmacia("farmacias.dat")
    arch.crearArchivoConDatos()

    # listar todas las farmacias con sus medicamentos
    arch.listar()

    # B mostrar medicamentos tipo "Tos" de una sucursal
    try:
        sucursalX = int(input("\nIngrese número de sucursal para mostrar medicamentos tipo 'Tos': "))
        arch.mostrarMedicamentosTosSucursal(sucursalX)
    except ValueError:
        print("Debe ingresar un número válido.")

    #C mostrar sucursales que tienen el medicamento "Golpex"
    arch.mostrarSucursalesConMedicamento("Golpex")
