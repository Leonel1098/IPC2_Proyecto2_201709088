from flask import Flask, redirect, render_template, request, url_for
from Carga_XML import cargaXml
app = Flask(__name__)
import os

upload_folder = './uploads/'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cargar_archivo_xml', methods=['POST'])
def cargar_archivo_xml():
    if 'archivo' not in request.files:
        print("No se ha seleccionado un archivo.", "error")
        return redirect(url_for('index'))

    archivo = request.files['archivo']
    if archivo.filename == '':
        print("Nombre de archivo vacío.", "error")
        return redirect(url_for('index'))

    if archivo and archivo.filename.endswith('.xml'):
        ruta_archivo = os.path.join(upload_folder, archivo.filename)
        archivo.save(ruta_archivo)

        # Cargar el XML
        maquinas, contenido_xml = cargaXml.lectura_xml(ruta_archivo)
        
        if maquinas is None:
            print("Error al leer el archivo XML.", "error")
            return redirect(url_for('index'))

        print("Archivo cargado exitosamente.", "success")
        return render_template('resultado.html', maquinas=maquinas, contenido_xml=contenido_xml)
    else:
        print("Formato de archivo no permitido.", "error")
        return redirect(url_for('index'))



@app.route('/simulate')
def simulate():
    return render_template('simulation.html')

if __name__ == '__main__':
    app.run(debug=True)
