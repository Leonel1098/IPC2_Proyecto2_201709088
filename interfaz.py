import xml.etree.ElementTree as ET
from tkinter import Tk
import tkinter as tk
from tkinter import * 
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from Drones import *
from Lista_Doble_Enlazada import *
from Altura import *
from System_Drones import *


listaPrincipal = Lista_Doble_Enlazada()
listaSistema = Lista_Doble_Enlazada()
listaDrones = Lista_Doble_Enlazada()
listaNiveles = Lista_Doble_Enlazada()

class interfaz ():

    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.title("ENCRIPTADOR DE MENSAJES")
        self.ventana.geometry("%dx%d+%d+%d" % (900,500,350,100))
        self.ventana.resizable(0,0)

        self.panel_Frame = Frame()
        self.panel_Frame.pack(side="top")
        self.panel_Frame.place(width="900", height="500")
        self.panel_Frame.config(background="black")

        self.button_inicializar = Button(self.panel_Frame, text = "Inicializar", command ="", foreground="white" )
        self.button_inicializar.pack()
        self.button_inicializar.config(bg="black")
        self.button_inicializar.place(x = 20, y = 18, width = 165, height = 40)

        self.button_cargar = Button(self.panel_Frame, text = "Cargar Archivo XML", command = self.CargarArchivo, foreground="white" )
        self.button_cargar.pack()
        self.button_cargar.config(bg="black")
        self.button_cargar.place(x = 20, y = 60, width = 165, height = 40)

        self.button_generar = Button(self.panel_Frame, text = "Generar Archivo XML", command ="", foreground="white" )
        self.button_generar.pack()
        self.button_generar.config(bg="black")
        self.button_generar.place(x = 20, y = 102, width = 165, height = 40)

        self.button_gestionar_drones = Button(self.panel_Frame, text = "Gestionar Drones", command ="", foreground="white" )
        self.button_gestionar_drones.pack()
        self.button_gestionar_drones.config(bg="black")
        self.button_gestionar_drones.place(x = 20, y = 144, width = 165, height = 40)

        self.button_gestionar_sistemas = Button(self.panel_Frame, text = "Gestionar Sistemas de Drones", command ="", foreground="white" )
        self.button_gestionar_sistemas.pack()
        self.button_gestionar_sistemas.config(bg="black")
        self.button_gestionar_sistemas.place(x = 20, y = 186, width = 165, height = 40)

        self.button_gestionar_mensajes = Button(self.panel_Frame, text = "Gestionar Mensajes", command ="", foreground="white" )
        self.button_gestionar_mensajes.pack()
        self.button_gestionar_mensajes.config(bg="black")
        self.button_gestionar_mensajes.place(x = 20, y = 230, width = 165, height = 40)

        self.button_ayuda = Button(self.panel_Frame, text = "Ayuda", command ="", foreground="white" )
        self.button_ayuda.pack()
        self.button_ayuda.config(bg="black")
        self.button_ayuda.place(x = 20, y = 272, width = 165, height = 40)


        self.campo_texto = ScrolledText(self.panel_Frame, wrap = tk.WORD)
        self.campo_texto.pack()
        self.campo_texto.place(x = 190, y = 18, width = 700, height = 475)
        
        
        self.campo_texto.bind('<Key>', )
        self.campo_texto.bind('<MouseWheel>')

        self.ventana.mainloop()


    def CargarArchivo(self):
        
        global listaPrincipal
        global listaSistema
        global listaDrones
        global listaNiveles
        
        
        tree = ET.parse('entradaV3.xml')
        root = tree.getroot()
        for sistema in  root.findall(".//listaSistemasDrones/sistemaDrones"):
            nombre_sistema = sistema.get("nombre")
            altura_max = sistema.find("alturaMaxima")
            cant_drones = sistema.find("cantidadDrones")
            if altura_max is not None :
                alturaMaxima = altura_max.text
            else:
                alturaMaxima = None
            if cant_drones is not None:
                cantidadDrones = cant_drones.text
            else:
                cantidadDrones = None
            print(nombre_sistema)
            print(alturaMaxima)
            print(cantidadDrones)
            for contenido in sistema.findall("contenido"):
                dron = contenido.find("dron").text
                alturas = contenido.find("alturas")
                print(dron)
                for altura in alturas.findall("altura"):
                    dato = altura.get("valor")
                    letra = altura.text
                    x1 = Altura(dato,letra)
                    listaNiveles.agregar_final(x1)
                y1 = Drones(dron, listaNiveles)
                listaDrones.agregar_final(y1)
                listaNiveles = Lista_Doble_Enlazada()
            x2 = System_Drones(nombre_sistema, altura_max, cant_drones, contenido)
            listaSistema.agregar_final(x2)
            listaDrones = Lista_Doble_Enlazada()
            
    def dronesPrincipales():
        pass


    """def CargarArchivo(self):
        global archivo_actual
        archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.XML")])
        archivo_texto = open(archivo, "r+", encoding="utf8")
        archivo_texto.close()
        tree = ET.parse(archivo)
        raiz = tree.getroot()

        for elemento in raiz.iter():
    # Obtener el nombre del elemento
            nombre_elemento = elemento.tag
    
    # Obtener el contenido del elemento (texto)
            contenido_elemento = elemento.text
    
    # Imprimir el nombre y contenido del elemento
            print(f"{nombre_elemento}: {contenido_elemento}")

        self.campo_texto.delete(1.0, tk.END)
        self.campo_texto.insert(tk.END, raiz)
        self.data = self.campo_texto.get(1.0, tk.END)
        self.data = raiz


    def Leer_Xml(self):
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        global archivo_actual
        archivo = filedialog.askopenfilename()
        print("Archivo seleccionado:", archivo)
        print("")
        archivo_texto = open(archivo, "r+", encoding = "utf8")
        archivo_texto.close()
        tree = ET.parse(archivo)
        raiz = tree.getroot()

        self.campo_texto.delete(1.0, tk.END)
        self.campo_texto.insert(tk.END, archivo_texto )
        def mostrar_elemento(elemento, nivel):
            espacios = "  " * nivel
            nombre_elemento = elemento.tag
            contenido_elemento = elemento.text
            self.campo_texto.insert(tk.END, f"{espacios}{nombre_elemento}: {contenido_elemento}\n")

            for hijo in elemento:
                mostrar_elemento(hijo, nivel + 1)

        mostrar_elemento(raiz, 0)

        

    lista_senalestemp = lista_senales()
    for senales_temporal in raiz.findall("senal"):
        nombre_senal = senales_temporal.get("nombre")
        tiempo_senal = senales_temporal.get("t")
        amplitud_senal = senales_temporal.get("A")
        print("")
        print(nombre_senal, tiempo_senal, amplitud_senal)

        lista_datostemp = lista_datos()
        lista_datosPatrones_temp = lista_datos()
        for dato_senal in senales_temporal.findall("dato"):
            tiempo_dato = dato_senal.get("t")
            amplitud_dato = dato_senal.get("A")
            frecuencia_dato = dato_senal.text

            nuevo_dato = datos(int(tiempo_dato),int(amplitud_dato),frecuencia_dato)
            lista_datostemp.insertar_dato(nuevo_dato)

            if frecuencia_dato != "0":
                nuevo_dato = datos(int(tiempo_dato),int(amplitud_dato),1)
                lista_datosPatrones_temp.insertar_dato(nuevo_dato)
            else:
                nuevo_dato = datos(int(tiempo_dato),int(amplitud_dato),0)
                lista_datosPatrones_temp.insertar_dato(nuevo_dato)
        
        lista_senalestemp.insertar_senal(senales(nombre_senal,tiempo_senal,amplitud_senal,lista_datostemp,lista_datosPatrones_temp))
    lista_senalestemp.recorre_imprimirLista_senal()
    global lista_senalestemp2
    lista_senalestemp2 = lista_senalestemp"""

interfaz()