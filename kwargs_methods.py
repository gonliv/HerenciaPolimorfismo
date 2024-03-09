class Persona:

  def __init__(self, **kwargs):
    for clave, valor in kwargs.items():
      setattr(self, clave, valor)


# Crear una instancia de la clase Persona con diferentes atributos
persona1 = Persona(nombre="Juan", edad=30, ciudad="Madrid")
persona2 = Persona(nombre="María", profesion="Ingeniera")

print(persona1.nombre, persona1.edad,
      persona1.ciudad)  # Salida: Juan 30 Madrid
print(persona2.nombre, persona2.profesion)  # Salida: María Ingeniera
