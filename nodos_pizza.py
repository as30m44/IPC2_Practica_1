from pizza import Pizza


class NodoS_Pizza():
  __siguiente = None # NodoS_Pizza()
  __pizza = Pizza() # Pizza()
  
  def __init__(self):
    pass
  
  def get_siguiente(self):
    return self.__siguiente
    
  def get_pizza(self):
    return self.__pizza
  
  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente
  
  def set_pizza(self, pizza):
    self.__pizza = pizza
  
  
  
  def desplegar(self, opcion):
    self.__pizza.desplegarFila(opcion)