class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        self.productos.pop(id, None)

    def actualizar_producto(self, id, nuevo_cantidad, nuevo_precio):
        if id in self.productos:
            self.productos[id].cantidad = nuevo_cantidad
            self.productos[id].precio = nuevo_precio

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                return producto
        return None

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        import pickle
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        import pickle
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado.")

            def menu():
                while True:
                    print("\nMenú:")
                    print("1. Agregar producto")
                    print("2. Eliminar producto")
                    print("3. Actualizar producto")
                    print("4. Buscar producto")
                    print("5. Mostrar todos los productos")
                    print("6. Guardar inventario")
                    print("7. Cargar inventario")
                    print("8. Salir")

                    opcion = input("Ingrese una opción: ")

                    if opcion == '1':
                    # ... (implementar agregar producto)
                    elif opcion == '2':
                # ... (implementar eliminar producto)
                # ... y así sucesivamente para las demás opciones
