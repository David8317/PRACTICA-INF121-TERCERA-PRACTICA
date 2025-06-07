
public class Main {
    public static void main(String[] args) {
        ArchivoCliente arch = new ArchivoCliente("clientes.dat");

        arch.crearArchivo();
        arch.guardaCliente(new Cliente(1, "Ana", 67890123));
        arch.guardaCliente(new Cliente(2, "Luis", 76543210));
        arch.guardaCliente(new Cliente(3, "Pedro", 71234567));

        //  por ID
        Cliente c1 = arch.buscarCliente(2);
        if (c1 != null)
            System.out.println("Cliente encontrado por ID: " + c1);
        else
            System.out.println("Cliente no encontrado.");

        //  por celular (también usando ID, pero mostramos el teléfono)
        Cliente c2 = arch.buscarCelularCliente(3);
        if (c2 != null)
            System.out.println("Cliente y su celular: " + c2.nombre + ", Teléfono: " + c2.telefono);
        else
            System.out.println("Cliente no encontrado.");
    }
}
