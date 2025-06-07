public class Producto {
    private String nombre;
    private double precio;

    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }
    
    @Override
    public String toString() {
        return "Producto{nombre='" + nombre + "', precio=" + precio + "}";
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Producto)) return false;
        Producto otro = (Producto) obj;
        return this.nombre.equals(otro.nombre) && this.precio == otro.precio;
    }
}

