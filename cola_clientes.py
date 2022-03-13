from nodoc_cliente import NodoC_Cliente



class Cola_Clientes():
  __nodoPrimero = None # NodoC_Cliente()
  __nodoUltimo = None # NodoC_Cliente()
  __nodoActual = None # NodoC_Cliente()
  __noCliente = 0
  __tiempo = 0
  
  def	__init__(self):
    pass

  def get_cliente(self):
    cliente = self.__nodoActual.get_cliente()
    return cliente

  def get_noCliente(self):
    return self.__noCliente
  
  
  
  def estaVacio(self):
    return self.__nodoPrimero == None and self.__nodoUltimo == None
  
  
  
  def insertarALaCola(self, cliente):
    cliente.set_idCliente(self.__noCliente + 1) # incrementar numeración al cliente
    self.__tiempo += cliente.get_tiempoEspera() # suma el tiempo de los nodos anteriores
    cliente.set_tiempoEspera(self.__tiempo)
    nodoNuevo = NodoC_Cliente()
    nodoNuevo.set_cliente(cliente)
    
    if (self.estaVacio()):
      self.__nodoPrimero = nodoNuevo
      self.__nodoUltimo = nodoNuevo
      self.__nodoActual = nodoNuevo
      self.__noCliente = 1
    else:
      self.__nodoUltimo.set_siguiente(nodoNuevo)
      self.__nodoUltimo = nodoNuevo
      self.__noCliente += 1
  
  
  
  def eliminarDeLaCola(self):
    if (self.estaVacio()):
      print("CLIENTE: ya no hay órdenes por preparar")
    else:
      # Eliminar el primer nodo de la cola
      self.__nodoPrimero.desplegarColumna()
      if (self.__nodoPrimero.get_siguiente() == None):
        self.__nodoPrimero = None
        self.__nodoUltimo = None
        self.__nodoActual = None
      else:
        self.__nodoPrimero = self.__nodoPrimero.get_siguiente()
      # Re-enumerar los clientes de la lista
      nodo_n = self.__nodoPrimero
      idCliente = 0
      while (nodo_n != None):
        idCliente += 1
        cliente_n = nodo_n.get_cliente()
        cliente_n.set_idCliente(idCliente)
        nodo_n.set_cliente(cliente_n)
        nodo_n = nodo_n.get_siguiente()
      

  
  
  def desplegar(self):
    if (self.estaVacio()):
      print("CLIENTE: No hay clientes en espera")
    else:
      nodo_n = self.__nodoPrimero
      nodo_n.get_cliente().desplegarTituloFila()
      while (nodo_n != None):
        nodo_n.desplegarFila()
        nodo_n = nodo_n.get_siguiente()
    