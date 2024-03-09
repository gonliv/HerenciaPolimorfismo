class Vehiculo:

  def describir(self):
    return "Este es un vehículo genérico."


class Coche(Vehiculo):

  def describir(self):
    descripcion_base = super().describir()
    return f"{descripcion_base} Es un coche."


coche = Coche()
print(coche.describir())
