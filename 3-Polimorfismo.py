class Animal:

  def hacer_sonido(self):
    pass


class Perro(Animal):

  def hacer_sonido(self):
    return "¡Guau!"


class Gato(Animal):

  def hacer_sonido(self):
    return "¡Miau!"


def hacer_sonido_animal(animal):
  return animal.hacer_sonido()


# Crear instancias de las subclases
perro = Perro()
gato = Gato()

# Llamar al mismo método con diferentes tipos de objetos
print(hacer_sonido_animal(perro))  # Salida: ¡Guau!
print(hacer_sonido_animal(gato))  # Salida: ¡Miau!
