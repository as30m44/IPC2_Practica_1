from listas_ingredientes import ListaS_Ingredientes



class Pizza():
  def __int__(self):
    self.__idPizza = 0 # se veran en el munu principal
    self.__especialidad = 0 # se veran en el munu principal
    self.__tiempoElaboracion = 0 # se veran en el munu principal
    self.__cantidad = 0 # se veran en el munu principal
    self.__listaIngredientes = ListaS_Ingredientes() # estará disponible en una opcion aparte

  def get_idPizza(self):
    return self.__idPizza

  def get_especialidad(self):
    return self.__especialidad

  def get_tiempoElaboracion(self):
    return self.__tiempoElaboracion

  def get_cantidad(self):
    return self.__cantidad

  def get_listaIngredientes(self):
    return self.__listaIngredientes
  
  def set_idPizza(self, idPizza):
    self.__idPizza = idPizza
  
  def set_especialidad(self, especialidad):
    self.__especialidad = especialidad
  
  def set_tiempoElaboracion(self, tiempoElaboracion):
    self.__tiempoElaboracion = tiempoElaboracion
  
  def set_cantidad(self, cantidad):
    self.__cantidad = cantidad
  
  def set_listaIngredientes(self, listaIngredientes):
    self.__listaIngredientes = listaIngredientes
    
    
    
  def desplegarTitulo(self):
    id = "|" + str("No").rjust(5, " ")
    especialidad = "|" + str("ESPECIALIDAD").center(10, " ")
    tiempo = "|" + str("TIEMPO").center(10, " ") + "|"
    cantidad = "|" + str("CANTIDAD").center(10, " ") + "|"
    borde = str("=").ljust(31, "=")
    print(borde)
    print(id, especialidad, tiempo, cantidad)
    print(borde)


  
  def desplegar(self):
    id = "|" + str(self.__idPizza).rjust(5, " ")
    especialidad = "|" + str(self.__especialidad).center(10, " ")
    tiempo = "|" + str(self.__tiempoElaboracion).center(10, " ") + "|"
    cantidad = "|" + str(self.__cantidad).center(10, " ") + "|"
    borde = str("-").ljust(31, "-")
    print(id, especialidad, tiempo, cantidad)
    print(borde)