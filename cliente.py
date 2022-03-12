from listas_pizzas import ListaS_Pizzas



class Cliente():
  def __init__(self):
    self.__idCliente = 0
    self.__nombre = ""
    self.__direccion = ""
    self.__municipio = ""
    self.__departamento = ""
    self.__listaPizzas = ListaS_Pizzas()
  
  def get_idCliente(self):
    return self.__idCliente

  def get_nombre(self):
    return self.__nombre

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

  def set_direccion(self, direccion):
    self.__direccion = direccion

  def set_municipio(self, municipio):
    self.__municipio = municipio

  def set_departamento(self, departamento):
    self.__departamento = departamento

  def set_listaPizzas(self, listaPizzas):
    self.__listaPizzas = listaPizzas
    
    
    
  def desplegarTituloFila(self):
    id = "|" + str("No").rjust(5, " ")
    nombre = "|" + str("NOMBRE").center(10, " ")
    direccion = "|" + str("DIRECCION").center(10, " ") + "|"
    municipio = "|" + str("MUNICIPIO").center(10, " ") + "|"
    departamento = "|" + str("DEPARTAMENTO").center(10, " ") + "|"
    borde = str("=").ljust(31, "=")
    print(borde)
    print(id, nombre, direccion, municipio, departamento)
    print(borde)


    
  def desplegarFila(self):
    id = "|" + str(self.__idCliente).rjust(5, " ")
    nombre = "|" + str(self.__nombre).center(10, " ")
    direccion = "|" + str(self.__direccion).center(10, " ") + "|"
    municipio = "|" + str(self.__municipio).center(10, " ") + "|"
    departamento = "|" + str(self.__departamento).center(10, " ") + "|"
    borde = str("-").ljust(31, "-")
    print(id, nombre, direccion, municipio, departamento)
    print(borde)
  
  
  
  def desplegarColumna(self):
    idT = "|" + str("No").rjust(5, " ")
    id = "|" + str(self.__idCliente).rjust(5, " ")
    nombreT = "|" + str("Nombre:").rjust(5, " ")
    nombre = "|" + str(self.__nombre).rjust(5, " ")
    direccionT = "|" + str("Direccion:").rjust(5, " ")
    direccion = "|" + str(self.__direccion).rjust(5, " ")
    municipioT = "|" + str("Municipio:").rjust(5, " ")
    municipio = "|" + str(self.__municipio).rjust(5, " ")
    departamentoT = "|" + str("Departamento:").rjust(5, " ")
    departamento = "|" + str(self.__departamento).rjust(5, " ")
    print(idT, id)
    print(nombreT, nombre)
    print(direccionT, direccion)
    print(municipioT, municipio)
    print(departamentoT, departamento)