class Libro:
    def __init__(self, isbn, titulo_autor, categoria):
        self.isbn = isbn
        self.titulo_autor = titulo_autor  # Tupla (titulo, autor)
        self.categoria = categoria

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario: ISBN -> Libro
        self.usuarios = set()  # Conjunto de IDs de usuario
        self.prestamos = {}  # Diccionario: ID usuario -> Lista de ISBNs

    # ... (métodos a implementar)



# Añadir libro
def agregar_libro(self, libro):
    self.libros[libro.isbn] = libro

# Quitar libro
def quitar_libro(self, isbn):
    self.libros.pop(isbn, None)

# Registrar usuario
def registrar_usuario(self, usuario):
    if usuario.id_usuario not in self.usuarios:
        self.usuarios.add(usuario.id_usuario)
        self.prestamos[usuario.id_usuario] = []
    else:
        print("Usuario ya existe")

# ... (implementar otras funcionalidades)

# Prestar libro
def prestar_libro(self, id_usuario, isbn):
    if id_usuario in self.usuarios and isbn in self.libros:
        if isbn not in self.prestamos[id_usuario]:
            self.prestamos[id_usuario].append(isbn)
        else:
            print("Libro ya prestado")
    else:
        print("Usuario o libro no encontrado")

        # Buscar libro por título
        def buscar_libro_por_titulo(self, titulo):
            for libro in self.libros.values():
                if titulo in libro.titulo_autor[0]:
                    print(libro)

        # Listar libros prestados por usuario
        def listar_libros_prestados(self, id_usuario):
            if id_usuario in self.prestamos:
                for isbn in self.prestamos[id_usuario]:
                    print(self.libros[isbn])
            else:
                print("Usuario no encontrado")