from flask import Flask, render_template, request
from Carga_XML import cargaXml
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cargar_archivo_xml', methods=['POST'])
def cargar_archivo_xml():
    if 'archivo' not in request.files:
        return "No se ha seleccionado un archivo", 400

    archivo = request.files['archivo']
    if archivo.filename == '':
        return "Nombre de archivo vacío", 400
    
    if archivo and archivo.filename.endswith('.xml'):
        # Guardar el archivo temporalmente
        ruta_archivo = f'./uploads/{archivo.filename}'
        archivo.save(ruta_archivo)

        # Cargar el XML con la función de nuestro archivo `cargar_xml.py`
        maquinas = cargaXml.cargar_xml(ruta_archivo)

        # Aquí puedes procesar los datos y renderizar una plantilla, por ejemplo
        return render_template('resultado.html', maquinas=maquinas)
    else:
        return "Formato de archivo no permitido", 400

@app.route('/simulate')
def simulate():
    return render_template('simulation.html')

if __name__ == '__main__':
    app.run(debug=True)
