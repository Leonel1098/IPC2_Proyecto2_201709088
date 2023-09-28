import xml.etree.ElementTree as ET
from tkinter import Tk
import tkinter as tk
from tkinter import * 
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog

"""def Leer_Xml():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    archivo = filedialog.askopenfilename()
    print("Archivo seleccionado:", archivo)
    print("")
    archivo_texto = open(archivo, "r+", encoding = "utf8")
    archivo_texto.close()
    tree = ET.parse(archivo)
    raiz = tree.getroot()

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

        self.button_cargar = Button(self.panel_Frame, text = "Cargar Archivo XML", command ="", foreground="white" )
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

interfaz()