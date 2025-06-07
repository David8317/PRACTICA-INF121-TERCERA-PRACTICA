class Libro {
    private String titulo;
    private String autor;

    public Libro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }
    @Override
    public String toString() {
        return "Libro{titulo='" + titulo + "', autor='" + autor + "'}";
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Libro)) return false;
        Libro otro = (Libro) obj;
        return this.titulo.equals(otro.titulo) && this.autor.equals(otro.autor);
    }
}

