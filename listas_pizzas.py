from turtle import pos
from nodos_pizza import NodoS_Pizza



class ListaS_Pizzas():
  __nodoInicio = None #NodosS_Pizza()
  __nodoFin = None #NodosS_Pizza()
  __nodoActual = None #NodosS_Pizza()
  __noPizzas = 0
  
  def __init__(self):
    pass
  
  def get_noPizzas(self):
    return self.__noPizzas
  
  def get_pizza(self):
    pizza = self.__nodoActual.get_pizza()
    return pizza
  
  
  
  def estaVacio(self):
    return self.__nodoInicio == None and self.__nodoFin == None
  
  
  
  def insertarAlFinal(self, pizza):
    nodoNuevo = NodoS_Pizza()
    pizza.set_idPizza(self.__noPizzas + 1)
    nodoNuevo.set_pizza(pizza)
    if (self.estaVacio()):
      self.__nodoInicio = nodoNuevo
      self.__nodoFin = nodoNuevo
      self.__nodoActual = nodoNuevo
      self.__noPizzas = 1
    else:
      self.__nodoFin.set_siguiente(nodoNuevo)
      self.__nodoFin = nodoNuevo
      self.__noPizzas += 1
  
  
  
  def ubicar(self, idPizza):
    self.__nodoActual = self.__nodoInicio
    pos_i = 1
    encontrado = False
    if (self.__nodoActual == None):
      print("PIZZA: El menú no tiene pizzas almacenadas")
    else:
      if (idPizza <= self.__noPizzas):
        while (encontrado == False):
          if (pos_i == idPizza):
            encontrado = True
          else:
            pos_i += 1
            self.__nodoActual = self.__nodoActual.get_siguiente()
      else:
        print("PIZZA: no se encuentra el item que ha ingresado")
  
  
  
  def desplegar(self, opcion):
    if (self.estaVacio()):
      print("PIZZA: El menú no tiene pizzas almacenadas")
    else:
      nodo_n = self.__nodoInicio
      nodo_n.get_pizza().desplegarTitulo(opcion)
      while (nodo_n != None):
        nodo_n.desplegar(opcion)
        nodo_n = nodo_n.get_siguiente()