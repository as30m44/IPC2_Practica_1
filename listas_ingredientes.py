from nodos_ingrediente import NodoS_Ingrediente



class ListaS_Ingredientes():
  def __init__(self):
    self.__nodoInicio = None # NodoS_Ingrediente()
    self.__nodoFinal = None # NodoS_Ingrediente()
    self.__nodoActual = None # NodoS_Ingrediente()
    self.__noIngredientes = 0
    
  
        
  def estaVacio(self):
    return (self.__nodoInicio == self.__nodoFinal)
  
  
  
  def insertarAlFinal(self, ingrediente):
    nodoNuevo = NodoS_Ingrediente()
    nodoNuevo.set_ingrediente(ingrediente)
    if (self.estaVacio()):
      self.__noIngredientes = 1
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
      self.__nodoActual = nodoNuevo
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo
      self.__noIngredientes += 1



  def ubicar(self, idIngrediente):
    self.__nodoActual = self.__nodoInicio
    if (idIngrediente <= self.__noIngredientes and self.__nodoActual != None):
      self.__nodoActual = self.__nodoActual.get_siguiente()
    else:
      print("INGREDIENTE: no se encuentra el item que ha ingresado")



  def modificar(self, nombre, cantidad):
    ingrediente_n = self.__nodoActual.get_ingrediente()
    ingrediente_n.set_nombre(nombre)
    ingrediente_n.set_cantidad(cantidad)

  
  
  def desplegar(self):
    if (self.estaVacio()):
      print("INGREDIENTE: No ha ingresado ingredientes en esta pizza")
    else:
      nodo_n = self.__nodoInicio
      nodo_n.get_ingrediente().desplegarTitulo()
      while (nodo_n != None):
        nodo_n.desplegar()
        nodo_n = nodo_n.get_siguiente()
