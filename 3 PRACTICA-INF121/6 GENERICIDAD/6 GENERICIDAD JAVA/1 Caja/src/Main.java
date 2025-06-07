public class Main {
    public static void main(String[] args) {
        Caja<Integer> cajaEnteros = new Caja<>();
        cajaEnteros.guardar(12);
        cajaEnteros.guardar(8);
        cajaEnteros.guardar(20);
        System.out.println("Contenido de cajaEnteros: " + cajaEnteros.obtener());

        Caja<String> cajaCadenas = new Caja<>();
        cajaCadenas.guardar("hola");
        cajaCadenas.guardar("mundo");
        System.out.println("Contenido de cajaCadenas: " + cajaCadenas.obtener());
    }
}