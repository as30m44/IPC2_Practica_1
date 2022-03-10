import imp
from nodoc_pizza import NodoC_Pizza



class Cola_Pizza():
  def __init__(self):
    self.__nodoPrimero = None # Cola_Pizza()
    self.__nodoUltimo = None # Cola_Pizza()
    self.__nodoActual = None # Cola_Pizza()
    
    
    
  def estaVacio(self):
    return self.__nodoPrimero == self.__nodoUltimo
  
  
  
  def insertarALaCola(self, pizza):
    nodoNuevo = NodoC_Pizza()
    