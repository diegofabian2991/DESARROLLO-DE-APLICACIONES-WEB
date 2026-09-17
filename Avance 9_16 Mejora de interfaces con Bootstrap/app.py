from flask import Flask, render_template

app = Flask(__name__)


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Productos
@app.route("/productos")
def productos():
    return render_template("productos.html")


# Clientes
@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


# Proveedores
@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")


# Facturación
@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html")


if __name__ == "__main__":
    app.run(debug=True)