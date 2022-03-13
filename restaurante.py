import os
import time
from cliente import Cliente
from cola_clientes import Cola_Clientes
from ingrediente import Ingrediente
from listas_ingredientes import ListaS_Ingredientes
from listas_pizzas import ListaS_Pizzas
from pizza import Pizza



class Restaurante():
  __colaClientes = Cola_Clientes()
  __listaPizzas = ListaS_Pizzas()
  __borde_1 = str("#").ljust(80,"#")
  __borde_2 = str("*").ljust(80,"*")
  __borde_3 = str("=").ljust(80,"=")
  __espacioVertical = "\n"
  
  def __init__(self) -> None:
    pass
  
  
  
  def __crearPizzaIngredientes(self):
    pepperoni = Pizza()
    salchicha = Pizza()
    carne = Pizza()
    queso = Pizza()
    pinia = Pizza()
    
    pepperoni.set_especialidad("Pepperoni")
    pepperoni.set_tiempoElaboracion(3)
    for i in range (0, 5, 1):
      ingrediente_n = Ingrediente()
      ingrediente_n.set_idIngrediente("ingrediente p" + str(i))
      ingrediente_n.set_cantidad(i)
      pepperoni.set_listaIngredientes(ingrediente_n)
    
    salchicha.set_especialidad("Salchicha")
    salchicha.set_tiempoElaboracion(4)
    for i in range (0, 5, 1):
      ingrediente_n = Ingrediente()
      ingrediente_n.set_idIngrediente("ingrediente p" + str(i))
      ingrediente_n.set_cantidad(i)
      salchicha.set_listaIngredientes(ingrediente_n)
    
    carne.set_especialidad("Carne")
    carne.set_tiempoElaboracion(10)
    for i in range (0, 5, 1):
      ingrediente_n = Ingrediente()
      ingrediente_n.set_idIngrediente("ingrediente p" + str(i))
      ingrediente_n.set_cantidad(i)
      carne.set_listaIngredientes(ingrediente_n)
    
    queso.set_especialidad("Queso")
    queso.set_tiempoElaboracion(5)
    for i in range (0, 5, 1):
      ingrediente_n = Ingrediente()
      ingrediente_n.set_idIngrediente("ingrediente p" + str(i))
      ingrediente_n.set_cantidad(i)
      queso.set_listaIngredientes(ingrediente_n)
    
    pinia.set_especialidad("Piña")
    pinia.set_tiempoElaboracion(2)
    for i in range (0, 5, 1):
      ingrediente_n = Ingrediente()
      ingrediente_n.set_idIngrediente("ingrediente p" + str(i))
      ingrediente_n.set_cantidad(i)
      pinia.set_listaIngredientes(ingrediente_n)
    
    self.__listaPizzas.insertarAlFinal(pepperoni)
    self.__listaPizzas.insertarAlFinal(salchicha)
    self.__listaPizzas.insertarAlFinal(carne)
    self.__listaPizzas.insertarAlFinal(queso)
    self.__listaPizzas.insertarAlFinal(pinia)
  
  
  
  def __nuevoCliente(self):
    opcionSalida = 1
    while (opcionSalida == 1):
      os.system("cls") # limpia la pantalla
      cliente_n = Cliente()
      listaPizzas_n = ListaS_Pizzas()
      seleccionPizza = 1
      opcionPizza = 1
      cantidadPizza = 0
      tiempoElaboracion = 0
      print(self.__borde_2)
      print("DATOS DEL CLIENTE".center(80, " "))
      print(self.__borde_2)
      print(self.__espacioVertical)
      nombre = input("Nombre".ljust(15, " ") + ": ")
      direccion = input("Direccion".ljust(15," ") + ": ")
      municipio = input("Municipio".ljust(15, " ") + ": ")
      departamento = input("Departamento ".ljust(15," ") + ": ")
      cliente_n.set_nombre(nombre)
      cliente_n.set_direccion(direccion)
      cliente_n.set_municipio(municipio)
      cliente_n.set_departamento(departamento)
      print(self.__espacioVertical)
      # Selección de pizza
      print(self.__borde_3)
      print("SELECCIÓN DE PIZZAS")
      print(self.__borde_3)
      self.__listaPizzas.desplegar("menu")
      while (seleccionPizza == 1):
        pizza_n = Pizza()
        noPizzasMenu = self.__listaPizzas.get_noPizzas() # tamaño de la lista de pizzas
        if (noPizzasMenu != 0):
          # seleccionar una pizza del menú
          opcionPizza = self.__inputEsNumero("seleccione una pizza:", 1, noPizzasMenu)
          self.__listaPizzas.ubicar(opcionPizza)
          pizza_n = self.__listaPizzas.get_pizza()
          # asignar la cantidad de pizzas
          cantidadPizza = self.__inputEsNumero("Ingrese el número de pizzas (entre 1 y 50 unidades):", 1, 50)
          pizza_n.set_cantidad(cantidadPizza)
          listaPizzas_n.insertarAlFinal(pizza_n)
        else:
          print("PIZZA: El menú no tiene pizzas almacenadas")
        pizza_n = None
        print(self.__espacioVertical)
        print("1. Agregar más pizzas a la orden")
        print("2. DATOS DEL CLIENTE...")
        seleccionPizza = self.__inputEsNumero("¿Cuál es su opción?:", 1, 2)
      # calcula el tiempo total de elaboración de todas las pizzas
      tiempoElaboracion
      for i in range(1, listaPizzas_n.get_noPizzas() + 1, 1):
        listaPizzas_n.ubicar(i)
        pizza_n = listaPizzas_n.get_pizza()
        tiempoElaboracion += (pizza_n.get_tiempoElaboracion() * pizza_n.get_cantidad())
      cliente_n.set_tiempoEspera(tiempoElaboracion)
      cliente_n.set_listaPizzas(listaPizzas_n)
      self.__colaClientes.insertarALaCola(cliente_n)
      # Sale de este módulo o ingresa un nuevo cliente
      os.system("cls") # limpia la pantalla
      print("1. Agregar más clientes")
      print("2. CONTROL DE PEDIDOS DE PIZZAS...")
      print(self.__espacioVertical, self.__espacioVertical)
      opcionSalida = self.__inputEsNumero("¿Cuál es su opción?:", 1, 2)
  
  
  
  def __verColaClientes(self):
    os.system("cls") # limpia la pantalla
    self.__colaClientes.desplegar()
    opcionSalida = 1
    while (opcionSalida == 1):
      print(self.__espacioVertical)
      print("1. Ver detalles de alguna orden: ")
      print("2. CONTROL DE PEDIDOS DE PIZZAS...")
      opcionSalida = self.__inputEsNumero("¿Cuál es su opción?:", 1, 2)
      print(self.__espacioVertical)
      if (opcionSalida == 1):
        noClientes = self.__colaClientes.get_noCliente()
        idCliente = self.__inputEsNumero("¿Ingrese el número del cliente:", 1, noClientes)
        self.__colaClientes.ubicar(idCliente)
        self.__inputEsCualquierTecla()
  
  
  
  # def 
  # Pantalla principal del programa
  def main(self):
    noOpcion = 0
    self.__crearPizzaIngredientes()
    while (noOpcion != 5):
      os.system("cls") # limpia la pantalla
      # menú principal
      print(self.__borde_1)
      print(str(" BIENVENIDO A LA FONDA DE DOÑA FLORINDA ").center(80, "#"))
      print(self.__borde_1)
      print(self.__espacioVertical, self.__espacioVertical)
      print(str("CONTROL DE PEDIDOS DE PIZZAS").center(80, " "))
      print(str("*").ljust(80,"*"))
      print("Ingrese el número de la opción que desea realizar")
      print("1. Datos del nuevo cliente")
      print("2. Entregar pizza(s)")
      print("3. Ver cola de clientes")
      print("4. Datos del desarrollador")
      #print("4. Agregar nueva especialidad (pizza) al menú")
      #print("5. Eliminar especialida (pizza) del menú")
      print("5. Salir del sistema")
      print(self.__espacioVertical, self.__espacioVertical)
      noOpcion = self.__inputEsNumero("¿Cuál es su opción?:", 1, 5)
      # acciones del menu
      if (noOpcion == 1): # nuevo cliente
        self.__nuevoCliente()
        # time.sleep(5)
      elif(noOpcion == 2): # entregar pizza
        self.__colaClientes.eliminarDeLaCola()
        self.__inputEsCualquierTecla()
      elif(noOpcion == 3): # cola de clientes
        self.__verColaClientes()
      elif(noOpcion == 4): #Datos de desarrollador
        print("Andres Gustavo Solís Martínez")
        print("Carné: 200715068")
        self.__inputEsCualquierTecla()
      # elif(opcion == 2):
      else:
        print("Opción no válida")
    print("Gracias por usar nuestro servicios")
  
  
  
  def __inputEsNumero(self, solicitud, opcionMin, opcionMax):
    esNumero = False
    numero = 0
    while (esNumero == False):
      valorIngresado = input(solicitud)
      if (str(valorIngresado).isdigit()):
        numero = int(valorIngresado)
        if (opcionMin <= numero and numero <= opcionMax):
          esNumero = True
        else:
          solicitud = "Esta opción no se encuentra, escriba otra: "
      else:
        solicitud = "únicamente se permiten números, escriba nuevamente una opción: "
    return numero
  
  
  
  def __inputEsCualquierTecla(self):
    solicitud = input("Presiona cualquier tecla para continuar: ")
    salir = False
    while (salir == False):
      if (solicitud != ""):
        salir = True
  
  
  
if (__name__ == '__main__'):
  sucursal_1 = Restaurante()
  sucursal_1.main()