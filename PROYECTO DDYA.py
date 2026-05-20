from sys import stdin

class Node:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

    def agregar_vecino(self, nodo):
        existe = existe_vecino(self.vecinos, nodo)
        if existe == False:
            self.vecinos.append(nodo)
            
def existe_usuario(lista_usuarios, nombre):
    encontrado = False
    i = 0
    while i < len(lista_usuarios):
        if lista_usuarios[i].nombre == nombre:
            encontrado = True
        i += 1
    return encontrado

def obtener_usuario(lista_usuarios, nombre):
    usuario = None
    i = 0
    while i < len(lista_usuarios):
        if lista_usuarios[i].nombre == nombre:
            usuario = lista_usuarios[i]
        i += 1
    return usuario

def existe_vecino(lista, nodo):
    encontrado = False
    i = 0
    while i < len(lista):
        if lista[i] == nodo:
            encontrado = True
        i += 1
    return encontrado

def existe_nombre(lista, nombre):
    encontrado = False
    i = 0
    while i < len(lista):
        if lista[i] == nombre:
            encontrado = True
        i += 1
    return encontrado

def imprimir_lista(lista):
    texto = ""
    i = 0
    while i < len(lista):
        texto += lista[i]
        if i < len(lista) - 1:
            texto += " "
        i += 1
    print(texto)

class Graph:
    def __init__(self):
        self.usuarios = []

    def crear_usuario(self, nombre):
        existe = existe_usuario(self.usuarios, nombre)
        if existe == False:
            nuevo_usuario = Node(nombre)
            self.usuarios.append(nuevo_usuario)

    def conectar(self, u, v):
        existe_u = existe_usuario(self.usuarios, u)
        existe_v = existe_usuario(self.usuarios, v)
        if existe_u == True and existe_v == True:
            nodo_u = obtener_usuario(self.usuarios, u)
            nodo_v = obtener_usuario(self.usuarios, v)
            nodo_u.agregar_vecino(nodo_v)
            nodo_v.agregar_vecino(nodo_u)

    def contar_amistades(self, usuario):
        existe = existe_usuario(self.usuarios, usuario)
        if existe == True:
            nodo = obtener_usuario(self.usuarios, usuario)
            return len(nodo.vecinos)
        return 0

def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    longitud = len(pila)
    if longitud == 0:
        return None
    eliminado = pila[longitud - 1]
    pila[:] = pila[:longitud - 1]
    return eliminado

def encolar(cola, elemento):
    cola.append(elemento)
    
def desencolar(cola):
    longitud = len(cola)
    if longitud == 0:
        return None
    eliminado = cola[0]
    cola[:] = cola[1:]
    return eliminado

def main():
    grafo = Graph()
    linea = stdin.readline()
    while linea != "":
        linea = linea.strip()
        if linea != "":
            partes = linea.split()
            comando = partes[0]
            if comando == "crear_usuario":
                grafo.crear_usuario(partes[1])
            elif comando == "conectar":
                grafo.conectar(partes[1], partes[2])
            elif comando == "contar":
                print(grafo.contar_amistades(partes[1]))
        linea = stdin.readline()
        
main()




    
