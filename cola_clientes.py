from nodoc_cliente import NodoC_Cliente



class Cola_Cliente():
  def	__init__(self):
    self.__nodoPrimero = None # NodoC_Cliente()
    self.__nodoUltimo = None # NodoC_Cliente()
    self.__nodoActual = None # NodoC_Cliente()
    self.__noCliente = 0

  def get_cliente(self):
    cliente = self.__nodoActual.get_cliente()
    return cliente
  
  
  
  def estaVacio(self):
    return self.__nodoPrimero == None and self.__nodoUltimo == None
  
  
  
  def insertarALaCola(self, cliente):
    nodoNuevo = NodoC_Cliente()
    nodoNuevo.set_pizza(cliente)
    if (self.estaVacio()):
      self.__nodoPrimero = nodoNuevo
      self.__nodoUltimo = nodoNuevo
      self.__nodoActual = nodoNuevo
      self.__noCliente = 1
    else:
      self.__nodoFin.set_siguiente(nodoNuevo)
      self.__nodoFin = nodoNuevo
      self.__noCliente += 1
  
  
  
  def eliminarDeLaCola(self):
    if (self.estaVacio()):
      print("CLIENTE: ya no ordenes por servir")
    else:
      self.__nodoPrimero.desplegarColumna()
      self.__nodoPrimero = self.__nodoPrimero.get_siguiente()
