from flask import Flask, render_template, redirect, url_for, flash

from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm


app = Flask(__name__)

# Clave para sesiones y protección CSRF de Flask-WTF
app.config["SECRET_KEY"] = "smartpredict-ai-clave-desarrollo"


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

productos_data = [
    {
        "id": 1,
        "nombre": "Sensor de vibración industrial",
        "categoria": "Sensores",
        "precio": 185.00,
        "stock": 12
    },
    {
        "id": 2,
        "nombre": "Sensor de temperatura IoT",
        "categoria": "Sensores",
        "precio": 95.50,
        "stock": 8
    },
    {
        "id": 3,
        "nombre": "Gateway industrial IoT",
        "categoria": "Conectividad",
        "precio": 320.00,
        "stock": 0
    },
    {
        "id": 4,
        "nombre": "Módulo de adquisición de datos",
        "categoria": "Automatización",
        "precio": 245.75,
        "stock": 5
    }
]


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
    return render_template(
        "productos.html",
        nombre_sistema=nombre_sistema,
        productos=productos_data
    )

# Formulario de productos
@app.route("/productos/nuevo", methods=["GET", "POST"])
def formulario_producto():
    form = ProductoForm()

    if form.validate_on_submit():
        nuevo_producto = {
            "id": len(productos_data) + 1,
            "nombre": form.nombre.data,
            "categoria": form.categoria.data,
            "precio": form.precio.data,
            "stock": form.stock.data
        }

        productos_data.append(nuevo_producto)

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
    app.run(debug=True)
