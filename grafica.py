from graphviz import Digraph
from cola_clientes import Cola_Clientes
from cliente import Cliente



class Grafica():
  # __nodos = []
  # __noClientes = 0
  __colaClientes = Cola_Clientes()
 
  def __init__(self,lista):
    self.__colaClientes = lista
  
  
  
  def crearGrafica(self):
    cliente_n = Cliente ()
    disposicion = ""
    grafica = Digraph(comment="Diagrama")
    noClientes = self.__colaClientes.get_noCliente()
    cliente_n = self.__colaClientes.get_cliente()
    idCliente = cliente_n.get_idCliente()
    nombre = cliente_n.get_nombre()
    # Creación de los nodos
    for i in range(1, noClientes + 1, 1):
      grafica.node(str(idCliente), nombre)
      disposicion += str(idCliente)
      grafica.edges([])
    
   
   
   
dot = Digraph(comment="Tabla")
dot.node('0','a1')
dot.node('1','b1')
dot.node('2','c1')
dot.node('3','d1')

dot.edges(['01','12', '23'])
# dot.edge('0','2',constraint='false')
print(dot.source)
dot.render('test-output/tabla.svg',view=True)