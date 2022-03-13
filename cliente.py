from listas_pizzas import ListaS_Pizzas



class Cliente():
  __idCliente = 0
  __nombre = ""
  __tiempoEspera = 0
  __direccion = ""
  __municipio = ""
  __departamento = ""
  __listaPizzas = ListaS_Pizzas()
  
  def __init__(self):
    pass
  
  def get_idCliente(self):
    return self.__idCliente

  def get_nombre(self):
    return self.__nombre

  def get_tiempoEspera(self):
    return self.__tiempoEspera

  def get_direccion(self):
    return self.__direccion

  def get_municipio(self):
    return self.__municipio

  def get_departamento(self):
    return self.__departamento

  def get_listaPizzas(self):
    return self.__listaPizzas

  def set_idCliente(self, idCliente):
    self.__idCliente = idCliente

  def set_nombre(self, nombre):
    self.__nombre = nombre

  def set_tiempoEspera(self, tiempoEspera):
    self.__tiempoEspera = tiempoEspera

  def set_direccion(self, direccion):
    self.__direccion = direccion

  def set_municipio(self, municipio):
    self.__municipio = municipio

  def set_departamento(self, departamento):
    self.__departamento = departamento

  def set_listaPizzas(self, listaPizzas):
    self.__listaPizzas = listaPizzas
    
    
    
  def desplegarTituloFila(self):
    id = "|" + str("No").center(5, " ")
    nombre = "|" + str("NOMBRE").center(15, " ")
    tiempo = "|" + str("TIEMPO").center(8, " ")
    direccion = "|" + str("DIRECCION").center(15, " ")
    municipio = "|" + str("MUNICIPIO").center(12, " ")
    departamento = "|" + str("DEPARTAMENTO").center(12, " ") + "|"
    borde = str("=").ljust(79, "=")
    print(borde)
    print(id, nombre, tiempo, direccion, municipio, departamento)
    print(borde)


    
  def desplegarFila(self):
    id = "|" + str(self.__idCliente).rjust(5, " ")
    nombre = "|" + str(self.__nombre).center(15, " ")
    tiempo = "|" + str(self.__tiempoEspera).center(8, " ")
    direccion = "|" + str(self.__direccion).center(15, " ")
    municipio = "|" + str(self.__municipio).center(12, " ")
    departamento = "|" + str(self.__departamento).center(12, " ") + "|"
    borde = str("-").ljust(79, "-")
    print(id, nombre, tiempo, direccion, municipio, departamento)
    print(borde)
  
  
  
  def desplegarColumna(self):
    idT = "|" + str("No").ljust(15, " ")
    id = ": " + str(self.__idCliente).ljust(25, " ") + "|"
    nombreT = "|" + str("Nombre").ljust(15, " ")
    nombre = ": " + str(self.__nombre).ljust(25, " ") + "|"
    tiempoT = "|" + str("TIEMPO").ljust(15, " ")
    tiempo = ": " + str(self.__tiempoEspera).ljust(25, " ") + "|"
    direccionT = "|" + str("Direccion").ljust(15, " ")
    direccion = ": " + str(self.__direccion).ljust(25, " ") + "|"
    municipioT = "|" + str("Municipio:").ljust(15, " ")
    municipio = ": " + str(self.__municipio).ljust(25, " ") + "|"
    departamentoT = "|" + str("Departamento:").ljust(15, " ")
    departamento = ": " + str(self.__departamento).ljust(25, " ") + "|"
    borde = str("-").ljust(45, "-")
    print(borde)
    print(idT, id)
    print(borde)
    print(nombreT, nombre)
    print(borde)
    print(tiempoT, tiempo)
    print(borde)
    print(direccionT, direccion)
    print(borde)
    print(municipioT, municipio)
    print(borde)
    print(departamentoT, departamento)
    print(borde)
