class Local: "La Esquina Del Sabor"
    # ...

class Plato: "Platos A La Carta"
    # ...

class Cliente:"Luis Argudo"
    # ...

class Pedido:"65"
    # ...

# Crear locales
local_italiano = Local("La Toscana", "Italiana", 15.0, 4.5)
local_mexicano = Local("El Sombrero", "Mexicana", 12.0, 4.2)

# Crear platos
pizza_margarita = Plato("Pizza Margarita", "Mozzarella, tomate y albahaca", 10.0, ["Mozzarella", "Tomate", "Albahaca"])
tacos_al_pastor = Plato("Tacos al Pastor", "Carne")
