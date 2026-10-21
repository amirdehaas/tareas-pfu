class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            a = self.cabeza
            while a.siguiente != None:
                a = a.siguiente
            a.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

    def mostrar_ultimo(self):
        a = self.cabeza
        while a.siguiente != None: a = a.siguiente
        print("ultimo nodo:", a.codigo)

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)


l = ListaEnlazada()
l.agregar("e01","sobre")
l.agregar("e02","paquete")
l.agregar("e03","documento")
print("lista enlazada:")
l.mostrar()
print()
l.mostrar_ultimo()
print()

c = Cola()
c.encolar("e01"); c.encolar("e02")
c.encolar("e03")
print("prueba fifo (cola):")
print(c.desencolar())
print(c.desencolar())
print(c.desencolar())
if c.desencolar() == None:
    print("la cola esta vacia")
print()

p = Pila()
p.apilar("e01")
p.apilar("e02"); p.apilar("e03")
print("prueba lifo (pila):")
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())
if p.desapilar() == None:
    print("la pila esta vacia")