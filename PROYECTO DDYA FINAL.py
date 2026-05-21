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

def ordenar(lista):
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if lista[j] > lista[j + 1]:
                elemento_temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = elemento_temporal
            j += 1
        i += 1
    return lista

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

    def sugerencias(self, inicio):
        existe = existe_usuario(self.usuarios, inicio)
        if existe == False:
            return []
        visitados = []
        cola = []
        sugeridos = []
        nodo_inicio = obtener_usuario(self.usuarios, inicio)
        encolar(cola, nodo_inicio)
        visitados.append(inicio)
        while len(cola) > 0:
            actual = desencolar(cola)
            i = 0
            while i < len(actual.vecinos):
                vecino = actual.vecinos[i]
                visitado = existe_nombre(visitados, vecino.nombre)
                if visitado == False:
                    visitados.append(vecino.nombre)
                    encolar(cola, vecino)
                    amigo_directo = existe_vecino(nodo_inicio.vecinos, vecino)
                    agregado = existe_nombre(sugeridos, vecino.nombre)
                    if vecino.nombre != inicio and amigo_directo == False and agregado == False:
                        sugeridos.append(vecino.nombre)
                i += 1
        ordenar(sugeridos)
        return sugeridos

    def grupos(self):
        visitados = []
        grupos = []
        i = 0
        while i < len(self.usuarios):
            nombre = self.usuarios[i].nombre
            revisado = existe_nombre(visitados, nombre)
            if revisado == False:
                grupo = []
                pila = []
                apilar(pila, self.usuarios[i])
                while len(pila) > 0:
                    actual = desapilar(pila)
                    visitado = existe_nombre(visitados, actual.nombre)
                    if visitado == False:
                        visitados.append(actual.nombre)
                        grupo.append(actual.nombre)
                        j = 0
                        while j < len(actual.vecinos):
                            vecino = actual.vecinos[j]
                            revisado_vecino = existe_nombre(visitados, vecino.nombre)
                            if revisado_vecino == False:
                                apilar(pila, vecino)
                            j += 1
                ordenar(grupo)
                grupos.append(grupo)
            i += 1
        return grupos

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
    linea = stdin.readline().strip()
    while linea != "":
        if linea != "":
            partes = linea.split()
            comando = partes[0]
            if comando == "crear_usuario":
                nombre = partes[1]
                grafo.crear_usuario(nombre)
            elif comando == "conectar":
                usuario_1 = partes[1]
                usuario_2 = partes[2]
                grafo.conectar(usuario_1, usuario_2)
            elif comando == "contar":
                usuario = partes[1]
                print(grafo.contar_amistades(usuario))
            elif comando == "sugerir":
                usuario = partes[1]
                sugerencias = grafo.sugerencias(usuario)
                imprimir_lista(sugerencias)
            elif comando == "grupos":
                grupos = grafo.grupos()
                i = 0
                while i < len(grupos):
                    imprimir_lista(grupos[i])
                    i += 1
        linea = stdin.readline()

main()




    
