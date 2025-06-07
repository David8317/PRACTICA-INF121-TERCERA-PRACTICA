import java.io.*;

class Cliente implements Serializable {
    private static final long serialVersionUID = 1L;
    public int id;
    public String nombre;
    public int telefono;

    public Cliente(int id, String nombre, int telefono) {
        this.id = id;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    @Override
    public String toString() {
        return "Cliente{id=" + id + ", nombre='" + nombre + "', telefono=" + telefono + "}";
    }
}

class ArchivoCliente {
    private String nomA;

    public ArchivoCliente(String n) {
        this.nomA = n;
    }

    public void crearArchivo() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
            System.out.println("Archivo creado: " + nomA);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void guardaCliente(Cliente c) {
        try {
            File f = new File(nomA);
            ObjectOutputStream oos;

            if (f.exists() && f.length() > 0) {
                MiObjectOutputStream mos = new MiObjectOutputStream(new FileOutputStream(f, true));
                mos.writeObject(c);
                mos.close();
            } else {
                oos = new ObjectOutputStream(new FileOutputStream(nomA));
                oos.writeObject(c);
                oos.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Cliente buscarCliente(int idBuscado) {
        Cliente encontrado = null;
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
            while (true) {
                Cliente c = (Cliente) ois.readObject();
                if (c.id == idBuscado) {
                    encontrado = c;
                    break;
                }
            }
        } catch (EOFException eof) {
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return encontrado;
    }

    public Cliente buscarCelularCliente(int idBuscado) {
        Cliente encontrado = null;
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
            while (true) {
                Cliente c = (Cliente) ois.readObject();
                if (c.id == idBuscado) {
                    encontrado = c;
                    break;
                }
            }
        } catch (EOFException eof) {
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return encontrado;
    }

    private static class MiObjectOutputStream extends ObjectOutputStream {
        public MiObjectOutputStream(OutputStream out) throws IOException {
            super(out);
        }

        @Override
        protected void writeStreamHeader() throws IOException {
            reset(); 
        }
    }
}
