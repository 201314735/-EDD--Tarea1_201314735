class Nodo:
    def __init__(self, id = None,valor=None, siguiente=None):
        self.id = id
        self.valor = valor
        self.siguiente = siguiente

class Lista:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
    def insertar(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento

        if self.ultimo!= None:
            self.ultimo.siguiente = elemento

        self.ultimo = elemento

    def modificar(self, id,elemento):
        if self.cabeza==None:
            return False
        if int(self.cabeza.id)==int(id):

            if(self.cabeza.id == self.ultimo.id):
                elemento.siguiente = self.cabeza.siguiente
                self.cabeza = elemento
                self.ultimo = elemento
            else:
                elemento.siguiente = self.cabeza.siguiente
                self.cabeza = elemento
            return True
        else:
            actual = self.cabeza
            anterior = actual
            while actual != None:
                if int(actual.id) == int(id):
                    elemento.siguiente = actual.siguiente
                    anterior.siguiente = elemento
                    return True
                anterior = actual
                actual = actual.siguiente
        return False

    def mostrar(self):
        Nodo = self.cabeza
        while (Nodo != None):
            print (str(Nodo.id) +". "+Nodo.valor)
            Nodo=Nodo.siguiente

    def eliminar(self,id):
        if self.cabeza==None:
            return False
        if int(self.cabeza.id)==int(id):
            self.cabeza = self.cabeza.siguiente
            return True
        else:
            actual = self.cabeza
            anterior = actual
            while actual != None:
                if int(actual.id) == int(id):
                    anterior.siguiente = actual.siguiente
                    return True
                anterior = actual
                actual = actual.siguiente
        return False

if __name__ == "__main__":
    lista = Lista()
    id = 1

    while (True):
        print("\nSeleccionar Opción:\n")
        print("1. Insertar.")
        print("2. Modificar.")
        print("3. Mostrar.")
        print("4. Eliminar.")

        opcion = input()
        if opcion == "1":
            valor = input("\nIngresar valor a Insertar\n")
            nodo = Nodo(id,valor)
            lista.insertar(nodo)
            id=id+1;
        elif opcion == "2":
            lista.mostrar()
            idc = input("Seleccione nodo a Modificar")
            val = input("Ingrese el nuevo valor")
            nodo = Nodo(idc,val)
            if(lista.modificar(idc,nodo)):
                print("Hecho")
            else:
                print("Error")
        elif opcion == "3":
            lista.mostrar()
        elif opcion == "4":
            lista.mostrar()
            idc = input("Seleccione nodo a Eliminar")
            if(lista.eliminar(idc)):
                print("Hecho")
            else:
                print("Error")