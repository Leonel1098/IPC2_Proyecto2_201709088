from Nodo import *

class Lista_Doble_Enlazada:
    def __init__(self):
        #Apuntadores de la lista para saber 
        #el tamaño y el primero y el ulitimo de la lista 
        self.primero = None
        self.ultimo = None 
        self.size = 0

    #Metodo de la lista cuando esta Vacia 
    def vacia(self):
        return self.primero == None
    # Metodo para Agregar un Elemento Al Final de la Lista 
    def agregar_final(self,dato):
        # Se Verifica si la lista esta Vacia 
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else :
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
            """
            se utiliza un auxliar para guardar el ultimo dato de la lista
            se agrega el dato a la lista se apunta el nodo hacia el dato 
            y el el otro nodo hacia null
            """
        self.size += 1 
        

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
            """
            se utiliza un auxliar para guardar el ultimo dato de la lista
            se agrega el dato a la lista se apunta el nodo hacia el dato 
            y el el otro nodo hacia null
            """
        self.size += 1

    #Imprime los Valores de las listas 

    def recorrer_inicio(self):
            aux = self.primero
            while aux:
                print(aux.dato) 
                aux = aux.siguiente
    "Para Recorrer de Fin a Inicio "
    def recorrer_fin(self):
            aux = self.ultimo
            while aux:
                print(aux.dato)
                aux = aux.anterior
    "Eliminar inicio "
    def eliminar_inicio(self):
        "Verificamos si la lista esta vacia en el metodo "
        if self.vacia():
            
            print("La Lista Esta Vacia")
        
        
        elif  self.primero.siguiente == None:
           # "Si solo tiene un Elemento y se queda vacia "
           
            self.primero = self.ultimo = None
            self.size = 0
        else:
           # "Se elimina el primero y se corren los otros valires "
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1
            """ 
            se hace el segundo el primero elemento 
            se hace que el anterior sea nullo 
            se reduce el tamaño de la lista 
            """
        
       # "Eliminar al Final "

    def eliminar_Final(self):
        if self.vacia():
            print("LIsta Vacia")
        elif self.primero.siguiente == None:
            #"Eliminando el primero y el unico "
            self.primero = self.ultimo = None
            self.size = 0 
        #si solo  hay mas datos en la lista 
        else:
            # el ultimo puntero va a apuntar al anterior
            self.ultimo = self.ultimo.anterior
            # el ultimo puntero del ultimo nodo debe apuntar a un null
            self.ultimo.siguiente = None
            self.size -=1

        
            


    def size(self):
        return self.size