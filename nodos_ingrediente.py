from ingrediente import Ingrediente


class NodoS_Ingrediente():
  __siguiente = None # NodoS_Ingrediente()
  __ingrediente = Ingrediente() # Ingrediente()
  
  def __init__(self):
    pass

  def get_siguiente(self):
    return self.__siguiente

  def get_ingrediente(self):
    return self.__ingrediente

  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente

  def set_ingrediente(self, ingrediente):
    self.__ingrediente = ingrediente



  def desplegar(self):
    self.__ingrediente.desplegar()