# Clase Padre
class Animal:

  def __init__(self, nombre):
    self.nombre = nombre

  def hacer_sonido(self):
    pass


# Herencia de una clase
class Perro(Animal):

  def hacer_sonido(self):
    return "¡Guau!"


class Gato(Animal):

  def hacer_sonido(self):
    return "¡Miau!"


# Instancias
perro = Perro("Bobby")
print(perro.nombre)  # Salida: Bobby
print(perro.hacer_sonido())  # Salida: ¡Guau!

gato = Gato("Misi")
print(gato.nombre)  # Salida: Misi
print(gato.hacer_sonido())  # Salida: ¡Miau!
