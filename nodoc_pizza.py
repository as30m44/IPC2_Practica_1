


class NodoC_Pizza():
  def __init__(self):
    self.__anterior = None # NodoC_Pizza()
    self.__pizza = None # Pizza()
    
  def get_anterior(self):
    return self.__anterior
    
  def get_pizza(self):
    return self.__pizza
  
  def set_anterior(self, anterior):
    self.__anterior = anterior
  
  def set_pizza(self, pizza):
    self.__pizza = pizza