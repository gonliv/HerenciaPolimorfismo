class A:

  def metodo_a(self):
    print("Método de clase A")


class B:

  def metodo_b(self):
    print("Método de clase B")


class C:

  def metodo_c(self):
    print("Método de clase C")


class D(A, B, C):

  def metodo_d(self):
    print("Método de clase D")


objeto_d = D()
objeto_d.metodo_a()  # Salida: Método de clase A
objeto_d.metodo_b()  # Salida: Método de clase B
objeto_d.metodo_c()  # Salida: Método de clase C
objeto_d.metodo_d()  # Salida: Método de clase D

# Saber de donde proviene la instancia
print(objeto_d.__class__)
# Saber de donde hereda la clase con la que se instancia
print(issubclass(objeto_d.__class__, A))
print(issubclass(objeto_d.__class__, B))
print(issubclass(objeto_d.__class__, C))
# Saber de donde herada la clase
print(D.__bases__)
