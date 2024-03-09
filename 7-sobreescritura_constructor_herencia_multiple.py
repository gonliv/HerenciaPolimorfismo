class ClaseA:

  def __init__(self, atributo_a):
    self.atributo_a = atributo_a
    print("Constructor de ClaseA")


class ClaseB:

  def __init__(self, atributo_b):
    self.atributo_b = atributo_b
    print("Constructor de ClaseB")


class ClaseC(ClaseA, ClaseB):

  def __init__(self, atributo_a, atributo_b, atributo_c):
    # Llamar explícitamente a los constructores de las superclases
    ClaseA.__init__(self, atributo_a)
    ClaseB.__init__(self, atributo_b)
    self.atributo_c = atributo_c
    print("Constructor de ClaseC")


# Crear una instancia de la subclase
objeto = ClaseC("valor_atributo_a", "valor_atributo_b", "valor_atributo_c")

print(objeto.atributo_a)  # Salida: valor_atributo_a
print(objeto.atributo_b)  # Salida: valor_atributo_b
print(objeto.atributo_c)  # Salida: valor_atributo_c
