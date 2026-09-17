import sqlite3
import os

from flask import Flask, render_template, redirect, url_for, flash

from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm


app = Flask(__name__)

# Clave para sesiones y protección CSRF de Flask-WTF
app.config["SECRET_KEY"] = "smartpredict-ai-clave-desarrollo"

# Ruta de la base de datos SQLite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "data", "smartpredict_ai.db")


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_db():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ==============================
# DATOS DEL SISTEMA
# ==============================

nombre_sistema = "SmartPredict AI"

empresa = {
    "nombre": "SmartPredict AI",
    "sector": "Mantenimiento predictivo industrial",
    "estado": "Activo"
}


# ==============================
# DATOS DE PRODUCTOS
# ==============================



# ==============================
# DATOS DE CLIENTES
# ==============================

clientes_data = [
    {
        "id": 1,
        "nombre": "Andes Energy",
        "sector": "Energía",
        "estado": "Activo"
    },
    {
        "id": 2,
        "nombre": "PetroIndustrial",
        "sector": "Industria petrolera",
        "estado": "Activo"
    },
    {
        "id": 3,
        "nombre": "TecnoManufactura",
        "sector": "Manufactura",
        "estado": "Pendiente"
    }
]


# ==============================
# DATOS DE PROVEEDORES
# ==============================

proveedores_data = [
    {
        "id": 1,
        "nombre": "Industrial Sensors Ecuador",
        "especialidad": "Sensores industriales",
        "estado": "Activo"
    },
    {
        "id": 2,
        "nombre": "IoT Solutions",
        "especialidad": "Conectividad IoT",
        "estado": "Activo"
    },
    {
        "id": 3,
        "nombre": "Automation Tech",
        "especialidad": "Automatización industrial",
        "estado": "Pendiente"
    }
]


# ==============================
# DATOS DE FACTURACIÓN
# ==============================

facturas_data = [
    {
        "numero": "FAC-001",
        "cliente": "Andes Energy",
        "total": 1250.00,
        "estado": "Pagada"
    },
    {
        "numero": "FAC-002",
        "cliente": "PetroIndustrial",
        "total": 2480.50,
        "estado": "Pendiente"
    },
    {
        "numero": "FAC-003",
        "cliente": "TecnoManufactura",
        "total": 875.75,
        "estado": "Pagada"
    }
]


# ==============================
# RUTAS
# ==============================

# Página principal
@app.route("/")
def inicio():
    return render_template(
        "index.html",
        nombre_sistema=nombre_sistema,
        empresa=empresa
    )


# Productos
@app.route("/productos")
def productos():
    conn = get_db_connection()

    productos = conn.execute("""
        SELECT id, nombre, categoria, precio, stock
        FROM productos
        ORDER BY id
    """).fetchall()

    conn.close()

    return render_template(
        "productos.html",
        nombre_sistema=nombre_sistema,
        productos=productos
    )

# Formulario de productos
@app.route("/productos/nuevo", methods=["GET", "POST"])
def formulario_producto():
    form = ProductoForm()

    if form.validate_on_submit():
        conn = get_db_connection()

        conn.execute("""
            INSERT INTO productos (nombre, categoria, precio, stock)
            VALUES (?, ?, ?, ?)
        """, (
            form.nombre.data,
            form.categoria.data,
            form.precio.data,
            form.stock.data
        ))

        conn.commit()
        conn.close()

        flash("Producto registrado correctamente.", "success")
        return redirect(url_for("productos"))

    return render_template(
        "formulario_producto.html",
        nombre_sistema=nombre_sistema,
        form=form
    )

# Clientes
@app.route("/clientes")
def clientes():
    return render_template(
        "clientes.html",
        nombre_sistema=nombre_sistema,
        clientes=clientes_data
    )

# Formulario de clientes
@app.route("/clientes/nuevo", methods=["GET", "POST"])
def formulario_cliente():
    form = ClienteForm()

    if form.validate_on_submit():
        nuevo_cliente = {
            "id": len(clientes_data) + 1,
            "nombre": form.nombre.data,
            "sector": form.sector.data,
            "estado": "Pendiente"
        }

        clientes_data.append(nuevo_cliente)

        flash("Cliente registrado correctamente.", "success")
        return redirect(url_for("clientes"))

    return render_template(
        "formulario_cliente.html",
        nombre_sistema=nombre_sistema,
        form=form
    )


# Proveedores
@app.route("/proveedores")
def proveedores():
    return render_template(
        "proveedores.html",
        nombre_sistema=nombre_sistema,
        proveedores=proveedores_data
    )

# Formulario de proveedores
@app.route("/proveedores/nuevo", methods=["GET", "POST"])
def formulario_proveedor():
    form = ProveedorForm()

    if form.validate_on_submit():
        nuevo_proveedor = {
            "id": len(proveedores_data) + 1,
            "nombre": form.nombre.data,
            "especialidad": form.especialidad.data,
            "estado": "Pendiente"
        }

        proveedores_data.append(nuevo_proveedor)

        flash("Proveedor registrado correctamente.", "success")
        return redirect(url_for("proveedores"))

    return render_template(
        "formulario_proveedor.html",
        nombre_sistema=nombre_sistema,
        form=form
    )


# Facturación
@app.route("/facturacion")
def facturacion():
    return render_template(
        "facturacion.html",
        nombre_sistema=nombre_sistema,
        facturas=facturas_data
    )

# Formulario de facturación
@app.route("/facturacion/nueva", methods=["GET", "POST"])
def formulario_facturacion():
    form = FacturacionForm()

    if form.validate_on_submit():
        nueva_factura = {
            "numero": form.numero.data,
            "cliente": form.cliente.data,
            "total": form.total.data,
            "estado": form.estado.data
        }

        facturas_data.append(nueva_factura)

        flash("Factura registrada correctamente.", "success")
        return redirect(url_for("facturacion"))

    return render_template(
        "formulario_facturacion.html",
        nombre_sistema=nombre_sistema,
        form=form
    )


if __name__ == "__main__":
    inicializar_db()
    app.run(debug=True)
