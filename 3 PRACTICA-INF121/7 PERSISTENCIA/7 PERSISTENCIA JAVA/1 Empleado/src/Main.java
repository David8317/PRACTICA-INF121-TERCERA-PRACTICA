public class Main {
    public static void main(String[] args) {
        ArchivoEmpleado arch = new ArchivoEmpleado("empleados.dat");

        arch.guardarEmpleado(new Empleado("Ana", 25, 3000));
        arch.guardarEmpleado(new Empleado("Luis", 30, 4500));
        arch.guardarEmpleado(new Empleado("Marta", 28, 3800));

        Empleado emp1 = arch.buscaEmpleado("Ana");
        System.out.println("Empleado encontrado: " + emp1);

        Empleado emp2 = arch.mayorSalario(3500);
        System.out.println("Primer empleado con salario mayor a 3500: " + emp2);
    }
}
