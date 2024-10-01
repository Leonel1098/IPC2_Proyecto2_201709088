import xml.etree.ElementTree as ET
from Lista_Enlazada import Lista_Enlazada  # Asegúrate de tener esta clase implementada
from Maquina import Maquina  # Asegúrate de tener esta clase implementada
from Producto import Producto  # Asegúrate de tener esta clase implementada

class cargaXml:
    @staticmethod
    def lectura_xml(archivo):
        try:
            arbol = ET.parse(archivo)
            raiz = arbol.getroot()
            lista_maquinas = Lista_Enlazada()

            for maquina in raiz.findall('Maquina'):
                nombre = maquina.find('NombreMaquina').text.strip()
                lineas = int(maquina.find('CantidadLineasProduccion').text.strip())
                componentes = int(maquina.find('CantidadComponentes').text.strip())
                tiempo = int(maquina.find('TiempoEnsamblaje').text.strip())
                
                maquina_obj = Maquina(nombre, lineas, componentes, tiempo)
                
                for producto in maquina.find('ListadoProductos').findall('Producto'):
                    nombre_producto = producto.find('nombre').text.strip()
                    elaboracion = producto.find('elaboracion').text.strip()
                    producto_obj = Producto(nombre_producto, elaboracion)
                    maquina_obj.productos.agregar(producto_obj)
                
                lista_maquinas.agregar(maquina_obj)

            # Devolver tanto la lista de máquinas como el contenido del XML
            return lista_maquinas, ET.tostring(raiz, encoding='unicode')
        except ET.ParseError:
            print("Error al parsear el archivo XML.")
            return None, None
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return None, None
