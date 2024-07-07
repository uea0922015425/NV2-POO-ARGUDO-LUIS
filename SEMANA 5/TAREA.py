def calcular_area_triangulo(base, altura):
  """
  Calcula el área de un triángulo.

  Args:
      base (float): La longitud de la base del triángulo.
      altura (float): La longitud de la altura del triángulo.

  Returns:
      float: El área del triángulo.
  """
  if not isinstance(base, float) or not isinstance(altura, float):
    raise TypeError("La base y la altura deben ser números flotantes.")
  if base <= 0 or altura <= 0:
    raise ValueError("La base y la altura deben ser valores positivos.")
  return (base * altura) / 2

def main():
  """
  Función principal del programa.
  """
  try:
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la longitud de la altura del triángulo: "))
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")
  except TypeError as error:
    print(f"Error: {error}")
  except ValueError as error:
    print(f"Error: {error}")

if __name__ == "__main__":
  main()
