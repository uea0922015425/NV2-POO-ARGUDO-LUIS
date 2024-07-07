# Clases base y derivadas

class Figura:
    """
    Clase base que representa una figura geométrica.

    Atributos:
        nombre (str): Nombre de la figura.

    Métodos:
        dibujar(self): Método abstracto que se implementa en las clases derivadas.
        obtener_nombre(self): Devuelve el nombre de la figura.
    """

    def __init__(self, nombre):
        self.__nombre = nombre

    def dibujar(self):
        raise NotImplementedError("El método dibujar() debe implementarse en las clases derivadas.")

    def obtener_nombre(self):
        return self.__nombre


class Circulo(Figura):
    """
    Clase derivada que representa un círculo.

    Atributos:
        radio (float): Radio del círculo.

    Métodos:
        dibujar(self): Dibuja un círculo en la consola.
        calcular_area(self): Calcula y devuelve el área del círculo.
        obtener_radio(self): Devuelve el radio del círculo.
        establecer_radio(self, nuevo_radio): Establece el radio del círculo.
    """

    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.__radio = radio

    def dibujar(self):
        print(f"Dibujando un círculo con nombre {self.obtener_nombre()} y radio {self.__radio}")

    def calcular_area(self):
        return 3.1415 * self.__radio * self.__radio

    def obtener_radio(self):
        return self.__radio

    def establecer_radio(self, nuevo_radio):
        if nuevo_radio > 0:
            self.__radio = nuevo_radio
        else:
            print("Error: El radio debe ser un valor positivo.")


# Creación de instancias y uso de métodos

circulo1 = Circulo("Circulo 1", 5)
circulo1.dibujar()
print(f"El área del círculo 1 es: {circulo1.calcular_area():.2f}")

circulo1.establecer_radio(10)
print(f"Nuevo radio del círculo 1: {circulo1.obtener_radio()}")
# Clases base y derivadas

class Figura:
    """
    Clase base que representa una figura geométrica.

    Atributos:
        nombre (str): Nombre de la figura.

    Métodos:
        dibujar(self): Método abstracto que se implementa en las clases derivadas.
        obtener_nombre(self): Devuelve el nombre de la figura.
    """

    def __init__(self, nombre):
        self.__nombre = nombre

    def dibujar(self):
        raise NotImplementedError("El método dibujar() debe implementarse en las clases derivadas.")

    def obtener_nombre(self):
        return self.__nombre


class Circulo(Figura):
    """
    Clase derivada que representa un círculo.

    Atributos:
        radio (float): Radio del círculo.

    Métodos:
        dibujar(self): Dibuja un círculo en la consola.
        calcular_area(self): Calcula y devuelve el área del círculo.
        obtener_radio(self): Devuelve el radio del círculo.
        establecer_radio(self, nuevo_radio): Establece el radio del círculo.
    """

    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.__radio = radio

    def dibujar(self):
        print(f"Dibujando un círculo con nombre {self.obtener_nombre()} y radio {self.__radio}")

    def calcular_area(self):
        return 3.1415 * self.__radio * self.__radio

    def obtener_radio(self):
        return self.__radio

    def establecer_radio(self, nuevo_radio):
        if nuevo_radio > 0:
            self.__radio = nuevo_radio
        else:
            print("Error: El radio debe ser un valor positivo.")


# Creación de instancias y uso de métodos

circulo1 = Circulo("Circulo 1", 5)
circulo1.dibujar()
print(f"El área del círculo 1 es: {circulo1.calcular_area():.2f}")

circulo1.establecer_radio(10)
print(f"Nuevo radio del círculo 1: {circulo1.obtener_radio()}")
circulo1.dibujar()
circulo1.dibujar()
