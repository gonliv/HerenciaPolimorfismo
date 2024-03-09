class Animal:
  pass


class Perro(Animal):
  pass


class Gato(Animal):
  pass


animal = Animal()
perro = Perro()
gato = Gato()

# animal es una instancia de la clase Animal?
print(isinstance(animal, Animal))  # True
print(isinstance(perro, Perro))  # True
print(isinstance(gato, Gato))  # True

print(isinstance(animal, Perro))  # False
print(isinstance(perro, Gato))  # False
