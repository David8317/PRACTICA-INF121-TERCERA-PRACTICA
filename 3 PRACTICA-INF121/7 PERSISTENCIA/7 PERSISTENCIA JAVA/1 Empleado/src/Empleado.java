import java.io.*;
import java.util.ArrayList;

class Empleado implements Serializable {
    private static final long serialVersionUID = 1L;
    public String nombre;
    public int edad;
    public double salario;

    public Empleado(String nombre, int edad, double salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Empleado(nombre='" + nombre + "', edad=" + edad + ", salario=" + salario + ")";
    }
}

class ArchivoEmpleado {
    private String nomA;

    public ArchivoEmpleado(String nomA) {
        this.nomA = nomA;
    }

    // a) Guardar empleado
    public void guardarEmpleado(Empleado emp) {
        ArrayList<Empleado> empleados = new ArrayList<>();

        File archivo = new File(nomA);
        if (archivo.exists()) {
            try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(archivo))) {
                empleados = (ArrayList<Empleado>) in.readObject();
            } catch (IOException | ClassNotFoundException e) {
                empleados = new ArrayList<>();
            }
        }

        empleados.add(emp);

        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(archivo))) {
            out.writeObject(empleados);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // b) Buscar por nombre
    public Empleado buscaEmpleado(String nombre) {
        File archivo = new File(nomA);
        if (!archivo.exists()) return null;

        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(archivo))) {
            ArrayList<Empleado> empleados = (ArrayList<Empleado>) in.readObject();
            for (Empleado emp : empleados) {
                if (emp.nombre.equals(nombre)) {
                    return emp;
                }
            }
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }

    // c) Buscar primer empleado con salario mayor
    public Empleado mayorSalario(double sueldo) {
        File archivo = new File(nomA);
        if (!archivo.exists()) return null;

        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(archivo))) {
            ArrayList<Empleado> empleados = (ArrayList<Empleado>) in.readObject();
            for (Empleado emp : empleados) {
                if (emp.salario > sueldo) {
                    return emp;
                }
            }
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }
}

