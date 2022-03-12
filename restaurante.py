import os
from cliente import Cliente
from cola_clientes import Cola_Clientes



class Restaurante():
  def __init__(self) -> None:
    self.__colaClientes = Cola_Clientes()
    self.__borde_1 = str("#").ljust(80,"#")
    self.__borde_2 = str("*").ljust(80,"#")
    self.__espacioVertical = "\n"
    
  
  
  
  def __nuevoCliente(self):
    cliente_n = Cliente()
    os.system("cls") # limpia la pantalla
    print(self.__borde_2)
    print("DATOS DEL CLIENTE")
    print(self.__borde_2)
    print(self.__espacioVertical)
    nombre = input("Nombre : ")
    direccion = input("Direccion : ")
    municipio = input("Municipio : ")
    departamento = input("Departamento : ")
    cliente_n.set_nombre(nombre)
    cliente_n.set_direccion(direccion)
    cliente_n.set_municipio(municipio)
    cliente_n.set_departamento(departamento)
    self.__colaClientes.insertarALaCola(cliente_n)
    self.__colaClientes.desplegar()
  
  
  
  def __entregarPizza(self):
    
  # Pantalla principal del programa
  def main(self):
    opcion = 0
    while (opcion != 6):
      os.system("cls") # limpia la pantalla
      # menú principal
      print(self.__borde_1)
      print(str(" BIENVENIDO A LA FONDA DE DOÑA FLORINDA ").center(80, "#"))
      print(self.__borde_1)
      print(self.__espacioVertical, self.__espacioVertical)
      print(str("Control de pedidos de pizzas").center(80, " "))
      print(str("*").ljust(80,"*"))
      print("Ingrese el número de la opción que desea realizar")
      print("1. Datos del nuevo cliente")
      print("2. Entregar pizza(s)")
      print("3. Ver cola de clientes")
      print("4. Agregar nueva especialidad (pizza) al menú")
      print("5. Eliminar especialida (pizza) del menú")
      print("6. Salir del sistema")
      print(self.__espacioVertical, self.__espacioVertical)
      opcion = self.__inputEsNumero("¿Cuál es su opción?:")
      # acciones del menu
      if (opcion == 1): # nuevo cliente
        self.__nuevoCliente()
      elif(opcion == 2):
      elif(opcion == 2):
      elif(opcion == 2):
      elif(opcion == 2):
      else:
    print("Gracias por usar nuestro servicios")
  
  
  
  def __inputEsNumero(self, solicitud):
    esNumero = False
    numero = 0
    while (esNumero == False):
      valorIngresado = input(solicitud)
      if (str(valorIngresado).isdigit()):
        numero = int(valorIngresado)
        esNumero = True
    return numero
  
  
  
  
if (__name__ == '__main__'):
  sucursal_1 = Restaurante()
  sucursal_1.main()