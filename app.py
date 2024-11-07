
from flask import Flask, request, render_template, redirect, url_for
from productosController import crear_producto, leer_productos, actualizar_producto, eliminar_producto

app = Flask(__name__)


@app.route('/')
def index():
    categoria = request.args.get('categoria')  
    productos = leer_productos(categoria)
    return render_template('index.html', productos=productos)


@app.route('/producto', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    crear_producto(nombre, categoria, precio, cantidad)
    return redirect(url_for('index'))


@app.route('/producto/<id>', methods=['POST'])
def actualizar(id):
    nuevos_datos = {
        "precio": float(request.form['precio']),
        "cantidad": int(request.form['cantidad'])
    }
    actualizar_producto(id, nuevos_datos)
    return redirect(url_for('index'))


@app.route('/producto/<id>/eliminar', methods=['POST'])
def eliminar(id):
    eliminar_producto(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

