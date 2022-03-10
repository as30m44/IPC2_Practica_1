


class Ingrediente():
  def __init__(self):
    self.__idIngrediente = 0
    self.__nombre = ""
    self.__cantidad = 0.00

  def get_nombre(self):
    return self.__nombre

  def get_cantidad(self):
    return self.__cantidad

  def set_nombre(self, nombre):
    self.__nombre = nombre

  def set_cantidad(self, cantidad):
    self.__cantidad = cantidad
    
    
    
  def desplegarTitulo(self):
    id = "|" + str("No").rjust(5, " ")
    nombre = "|" + str("NOMBRE").center(10, " ")
    cantidad = "|" + str("CANTIDAD").center(10, " ") + "|"
    borde = str("=").ljust(31, "=")
    print(borde)
    print(id, nombre, cantidad)
    print(borde)


    
  def desplegar(self):
    id = "|" + str(self.__idIngrediente).rjust(5, " ")
    nombre = "|" + str(self.__nombre).center(10, " ")
    cantidad = "|" + str(self.__cantidad).center(10, " ") + "|"
    borde = str("-").ljust(31, "-")
    print(id, nombre, cantidad)
    print(borde)