class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def get_total_price(self):
        total = 0
        for product in self.items:
            total += product.get_total_price()
        return total

def main():
    # Create a grocery store
    store_name = "Mi Tienda de Luisargudo"
    print(f"Bienvenido a {store_name}")

    # Create some products
    products = [
        Product("Leche", 2.50, 1),
        Product("Huevos", 3.00, 6),
        Product("Manzanas", 1.50, 2),
        Product("Pan", 1.00, 1),
        Product("Tomates", 0.75, 3),
            ]

    # Create a shopping cart
    cart = Cart()

    # Add products to the cart
    for product in products:
        print(f"Producto: {product.name}, Precio: ${product.price}, Cantidad: {product.quantity}")
        cart.add_product(product)

    # Calculate the total price
    total_price = cart.get_total_price()
    print(f"Total de la compra: ${total_price:.2f}")

    # Ask the customer if they want to checkout
    checkout = input("¿Desea proceder al pago? (Si/No): ").lower()

    if checkout == "si":
        print("Procesando pago...")
        # Simulate payment process
        print("Pago realizado con éxito!")
        print("¡Gracias por su compra!")
    else:
        print("Su compra ha sido cancelada.")

if __name__ == "__main__":
    main()