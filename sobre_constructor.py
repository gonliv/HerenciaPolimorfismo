class ClaseBase:

  def __init__(self, atributo):
    self.atributo = atributo


class SubClase(ClaseBase):

  def __init__(self, atributo, nuevo_atributo):
    super().__init__(atributo)  # Llama al constructor de la superclase
    self.nuevo_atributo = nuevo_atributo  # Agrega un nuevo atributo


# Crear una instancia de la subclase
objeto = SubClase("valor_atributo", "valor_nuevo_atributo")

print(objeto.atributo)  # Salida: valor_atributo
print(objeto.nuevo_atributo)  # Salida: valor_nuevo_atributo
