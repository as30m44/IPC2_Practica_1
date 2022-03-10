from nodos_ingrediente import NodoS_Ingrediente



class ListaS_Ingrediente():
  def __init__(self):
    self.__nodoInicio = None # ListaS_Ingrediente()
    self.__nodoFinal = None # ListaS_Ingrediente()
    self.__nodoActual = None # ListaS_Ingrediente()
    self.__noIngrediente = 0
    
    
    
  def estaVacio(self):
    return (self.__nodoInicio == self.__nodoFinal)
  
  
  
  def insertarAlFinal(self, ingrediente):
    nodoNuevo = NodoS_Ingrediente()
    nodoNuevo.set_ingrediente(ingrediente)
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFinal = nodoNuevo
      self.__nodoActual = nodoNuevo
      self.__noIngrediente = 1
    else:
      self.__nodoFinal.set_siguiente(nodoNuevo)
      self.__nodoFinal = nodoNuevo
      self.__noIngrediente += 1

      
      
  def desplegar(self):
    nodo_n = self.__nodoInicio
    nodo_n.get_ingrediente().desplegarTitulo()

    while (nodo_n != None):
      nodo_n.desplegar()
      nodo_n = nodo_n.get_siguiente()
