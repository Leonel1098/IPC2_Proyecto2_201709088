import xml.etree.ElementTree as ET
from Lista_Enlazada import Lista_Enlazada
from Maquina import Maquina
from Producto import Producto

class cargaXml:
    def cargar_xml(ruta_archivo):
        arbol = ET.parse(ruta_archivo)
        raiz = arbol.getroot()
        
        lista_maquinas = Lista_Enlazada()

        for maquina in raiz.findall('Maquina'):
            nombre = maquina.find('NombreMaquina').text.strip()
            lineas = int(maquina.find('CantidadLineasProduccion').text.strip())
            componentes = int(maquina.find('CantidadComponentes').text.strip())
            tiempo = int(maquina.find('TiempoEnsamblaje').text.strip())
            
            # Creamos la máquina
            maquina_obj = Maquina(nombre, lineas, componentes, tiempo)
            
            # Cargar productos para esa máquina
            for producto in maquina.find('ListadoProductos').findall('Producto'):
                nombre_producto = producto.find('nombre').text.strip()
                elaboracion = producto.find('elaboracion').text.strip()
                
                # Crear el objeto Producto y añadirlo a la lista de productos de la máquina
                producto_obj = Producto(nombre_producto, elaboracion)
                maquina_obj.productos.agregar(producto_obj)
            
            # Agregar la máquina a la lista de máquinas
            lista_maquinas.agregar(maquina_obj)
        
        return lista_maquinas