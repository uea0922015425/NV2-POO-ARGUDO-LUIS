class Producto:
    """
    Clase que representa un producto.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad del producto en stock.

    Métodos:
        __init__(self, nombre, precio, cantidad): Constructor que inicializa los atributos del producto.
        __del__(self): Destructor que imprime un mensaje cuando se elimina una instancia de producto.
        obtener_nombre(self): Devuelve el nombre del producto.
        obtener_precio(self): Devuelve el precio del producto.
        obtener_cantidad(self): Devuelve la cantidad del producto en stock.
        establecer_precio(self, nuevo_precio): Establece el nuevo precio del producto.
        vender_producto(self, cantidad_a_vender): Vende una cantidad específica del producto.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Constructor que inicializa los atributos del producto.

        Parámetros:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            cantidad (int): Cantidad del producto en stock.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"Producto '{self.nombre}' creado con precio {self.precio:.2f} y cantidad {self.cantidad}.")

    def __del__(self):
        """
        Destructor que imprime un mensaje cuando se elimina una instancia de producto.
        """
        print(f"Producto '{self.nombre}' eliminado.")

    def obtener_nombre(self):
        return self.nombre

    def obtener_precio(self):
        return self.precio

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.precio = nuevo_precio
        else:
            print("Error: El precio debe ser un valor positivo.")

    def vender_producto(self, cantidad_a_vender):
        if cantidad_a_vender <= self.cantidad:
            self.cantidad -= cantidad_a_vender
            print(f"Se vendieron {cantidad_a_vender} unidades del producto '{self.nombre}'.")
        else:
            print(f"Error: No hay suficientes unidades del producto '{self.nombre}' en stock. Stock disponible: {self.cantidad}.")


# Creación de instancias de producto y uso de métodos

producto1 = Producto("Laptop", 1200.00, 10)
producto1.obtener_nombre()  # 'Laptop'
producto1.obtener_precio()  # 1200.0
producto1.obtener_cantidad()  # 10

producto1.vender_producto(5)  # Se vendieron 5 unidades del producto 'Laptop'.
producto1.obtener_cantidad()  # 5

producto1.establecer_precio(1000.00)  # Precio del producto 'Laptop' actualizado a 1000.0.

del producto1  # Se elimina la instancia de producto 'Laptop'.
