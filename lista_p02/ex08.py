class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    def __len__(self):
        return self.paginas

livro = Livro("Python para Iniciantes", "Ana Silva", 300)
print(livro)
print("Número de páginas:", len(livro))