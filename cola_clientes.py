from nodoc_cliente import NodoC_Cliente



class Cola_Clientes():
  def	__init__(self):
    self.__nodoPrimero = None # NodoC_Cliente()
    self.__nodoUltimo = None # NodoC_Cliente()
    self.__nodoActual = None # NodoC_Cliente()
    self.__noCliente = 0

  def get_cliente(self):
    cliente = self.__nodoActual.get_cliente()
    return cliente

  def get_noCliente(self):
    return self.__noCliente
  
  
  
  def estaVacio(self):
    return self.__nodoPrimero == None and self.__nodoUltimo == None
  
  
  
  def insertarALaCola(self, cliente):
    nodoNuevo = NodoC_Cliente()
    cliente.set_idCliente(self.__noCliente + 1) # incrementar numeración al cliente
    nodoNuevo.set_pizza(cliente)
    if (self.estaVacio()):
      self.__noCliente = 1
      self.__nodoPrimero = nodoNuevo
      self.__nodoUltimo = nodoNuevo
      self.__nodoActual = nodoNuevo
    else:
      self.__nodoFin.set_siguiente(nodoNuevo)
      self.__nodoFin = nodoNuevo
      self.__noCliente += 1
  
  
  
  def eliminarDeLaCola(self):
    if (self.estaVacio()):
      print("CLIENTE: ya no hay órdenes por preparar")
    else:
      cliente = self.__nodoPrimero.get_cliente()
      self.__nodoPrimero.desplegarColumna()
      self.__nodoPrimero = self.__nodoPrimero.get_siguiente()
      self.__noCliente -= 1

  
  
  def desplegar(self):
    if (self.estaVacio()):
      print("CLIENTE: No hay clientes en espera")
    else:
      nodo_n = self.__nodoPrimero
      nodo_n.get_cliente().desplegarTituloFila()
      while (nodo_n != None):
        nodo_n.desplegarFila()
        nodo_n = nodo_n.get_siguiente()
    