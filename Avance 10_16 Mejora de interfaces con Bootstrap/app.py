from flask import Flask, render_template

app = Flask(__name__)


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


# Clientes
@app.route("/clientes")
def clientes():
    return render_template(
        "clientes.html",
        nombre_sistema=nombre_sistema,
        clientes=clientes_data
    )


# Proveedores
@app.route("/proveedores")
def proveedores():
    return render_template(
        "proveedores.html",
        nombre_sistema=nombre_sistema,
        proveedores=proveedores_data
    )


# Facturación
@app.route("/facturacion")
def facturacion():
    return render_template(
        "facturacion.html",
        nombre_sistema=nombre_sistema,
        facturas=facturas_data
    )


if __name__ == "__main__":
    app.run(debug=True)
