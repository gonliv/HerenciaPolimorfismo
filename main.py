class Animal:

  def __init__(self, nombre):
    self.nombre = nombre

  def hacer_sonido(self):
    pass


class Perro(Animal):

  def hacer_sonido(self):
    return "¡Guau!"


class Gato(Animal):

  def hacer_sonido(self):
    return "¡Miau!"


perro = Perro("Bobby")
print(perro.nombre)  # Salida: Bobby
print(perro.hacer_sonido())  # Salida: ¡Guau!

gato = Gato("Misi")
print(gato.nombre)  # Salida: Misi
print(gato.hacer_sonido())  # Salida: ¡Miau!
# Saber de donde hereda la instancia
print(perro.__class__)
print(issubclass(perro.__class__, Gato))
# Saber de donde herada la clase
print(Perro.__bases__)
