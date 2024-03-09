def funcion(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")


# Llamada a la función con diferentes argumentos de palabra clave
funcion(nombre="Juan", edad=30, ciudad="Madrid")
