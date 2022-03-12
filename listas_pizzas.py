from nodos_pizza import NodoS_Pizza



class ListaS_Pizzas():
  def __init__(self) -> None:
    self.__nodoInicio = None #NodosS_Pizza()
    self.__nodoFin = None #NodosS_Pizza()
    self.__nodoActual = None #NodosS_Pizza()
    self.__noPizzas = 0
  
  def get_pizza(self):
    pizza = self.__nodoActual.get_pizza()
    return pizza
  
  
  
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFin == None
  
  
  
  def insertarAlFinal(self, pizza):
    nodoNuevo = NodoS_Pizza()
    nodoNuevo.set_pizza(pizza)
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFin = nodoNuevo
      self.__nodoActual = nodoNuevo
      self.__noPizzas = 1
    else:
      self.__nodoFin.set_nodoSiguiente(nodoNuevo)
      self.__nodoFin = nodoNuevo
      self.__noPizzas += 1
  
  
  
  def ubicar(self, idPizza):
    self.__nodoInicio = self.__nodoInicio
    if (idPizza <= self.__noPizzas and self.__nodoActual != None):
      self.__nodoActual = self.__nodoActual.get_siguiente()
    else:
      print("PIZZA: no se encuentra el item que ha ingresado")
  
  
  
  def desplegar(self):
    nodo_n = self.__nodoInicio
    nodo_n.get_pizza().desplegarTitulo()
    while (nodo_n != None):
      nodo_n.desplegar()
      nodo_n = nodo_n.get_siguiente()