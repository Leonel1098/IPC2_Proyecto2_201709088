from Lista_Enlazada import Lista_Enlazada
class Maquina:
    def __init__(self, nombre, lineas_produccion, componentes, tiempo_ensamblaje):
        self.nombre = nombre
        self.lineas_produccion = lineas_produccion
        self.componentes = componentes
        self.tiempo_ensamblaje = tiempo_ensamblaje
        self.productos = Lista_Enlazada()  
