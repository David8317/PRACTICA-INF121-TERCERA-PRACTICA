public class Main {
    public static void main(String[] args) {
        // c) 

        Pila<Integer> pilaEnteros = new Pila<>();
        pilaEnteros.apilar(10);
        pilaEnteros.apilar(20);
        pilaEnteros.apilar(30);

        System.out.println("Pila de enteros:");
        System.out.println(pilaEnteros.mostrar());

        System.out.println("Desapilando: " + pilaEnteros.desapilar());
        System.out.println("Pila de enteros después de desapilar:");
        System.out.println(pilaEnteros.mostrar());

        Pila<String> pilaCadenas = new Pila<>();
        pilaCadenas.apilar("Hola");
        pilaCadenas.apilar("Mundo");

        System.out.println("\nPila de cadenas:");
        System.out.println(pilaCadenas.mostrar());

        System.out.println("Desapilando: " + pilaCadenas.desapilar());
        System.out.println("Pila de cadenas después de desapilar:");
        System.out.println(pilaCadenas.mostrar());
    }
}
