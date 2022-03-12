from pizza import Pizza


class NodoS_Pizza():
  def __init__(self):
    self.__siguiente = None # NodoS_Pizza()
    self.__pizza = Pizza() # Pizza()
    
  def get_siguiente(self):
    return self.__siguiente
    
  def get_pizza(self):
    return self.__pizza
  
  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente
  
  def set_pizza(self, pizza):
    self.__pizza = pizza
  
  
  
  def deslplegar(self):
    self.__pizza.desplegar()