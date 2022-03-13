from cliente import Cliente



class NodoC_Cliente():
  __siguiente = None # NodoC_Cliente()
  __cliente = Cliente()
  
  def __init__(self):
    pass
  
  def get_siguiente(self):
    return self.__siguiente
  
  def get_cliente(self):
    return self.__cliente
  
  def set_siguiente(self, siguiente):
    self.__siguiente = siguiente
  
  def set_cliente(self, cliente):
    self.__cliente = cliente
  
  
  
  def desplegarFila(self):
    self.__cliente.desplegarFila()
  
  
  
  def desplegarColumna(self):
    self.__cliente.desplegarColumna()
    self.__cliente.get_listaPizzas().desplegar("cliente")