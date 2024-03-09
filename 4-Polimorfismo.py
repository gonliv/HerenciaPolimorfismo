class Figura:

  def calcular_area(self):
    pass


class Cuadrado(Figura):

  def __init__(self, lado):
    self.lado = lado

  def calcular_area(self):
    return self.lado**2


class Triangulo(Figura):

  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return 0.5 * self.base * self.altura


cuadrado = Cuadrado(5)
triangulo = Triangulo(4, 3)

print("Área del cuadrado:", cuadrado.calcular_area())  # Salida: 25
print("Área del triángulo:", triangulo.calcular_area())  # Salida: 6.0
