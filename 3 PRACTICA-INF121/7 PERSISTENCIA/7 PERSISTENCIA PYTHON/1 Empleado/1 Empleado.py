import pickle
import os

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"Empleado(nombre='{self.nombre}', edad={self.edad}, salario={self.salario})"

class ArchivoEmpleado:
    def __init__(self, nomA):
        self.nomA = nomA

    # a) Guardar empleado
    def guardarEmpleado(self, emp):
        empleados = []
        if os.path.exists(self.nomA):
            with open(self.nomA, "rb") as archivo:
                try:
                    empleados = pickle.load(archivo)
                except EOFError:
                    empleados = []
        empleados.append(emp)
        with open(self.nomA, "wb") as archivo:
            pickle.dump(empleados, archivo)

    # b) Buscar por nombre
    def buscaEmpleado(self, nombre):
        if not os.path.exists(self.nomA):
            return None
        with open(self.nomA, "rb") as archivo:
            empleados = pickle.load(archivo)
            for emp in empleados:
                if emp.nombre == nombre:
                    return emp
        return None

    # c) Buscar primer empleado con salario mayor 
    def mayorSalario(self, sueldo):
        if not os.path.exists(self.nomA):
            return None
        with open(self.nomA, "rb") as archivo:
            empleados = pickle.load(archivo)
            for emp in empleados:
                if emp.salario > sueldo:
                    return emp
        return None

def main():
    arch = ArchivoEmpleado("empleados.bin")

    arch.guardarEmpleado(Empleado("Ana", 25, 3000))
    arch.guardarEmpleado(Empleado("Luis", 30, 4500))
    arch.guardarEmpleado(Empleado("Marta", 28, 3800))

    emp = arch.buscaEmpleado("Ana")
    print("Empleado encontrado:", emp)

    emp2 = arch.mayorSalario(3500)
    print("Primer empleado con salario mayor a 3500:", emp2)

if __name__ == "__main__":
    main()
