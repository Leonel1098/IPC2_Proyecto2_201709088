from Nodo import Nodo


class Lista_Enlazada:

    def __init__(self):
        self.primero = None
    
    def agregar(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo
    
    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.data)
            actual = actual.next