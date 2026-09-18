from flask import Flask, render_template, redirect, url_for, flash

from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm

from conexion.conexion import obtener_conexion


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
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            p.id_producto,
            p.nombre,
            p.categoria,
            p.precio,
            p.stock,
            p.id_proveedor,
            pr.nombre AS proveedor
        FROM productos p
        LEFT JOIN proveedores pr
            ON p.id_proveedor = pr.id_proveedor
        ORDER BY p.id_producto
    """)

    productos = cursor.fetchall()

    cursor.close()
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

    # Cargar proveedores desde MySQL
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_proveedor, nombre
        FROM proveedores
        ORDER BY nombre
    """)

    proveedores = cursor.fetchall()

    cursor.close()
    conn.close()

    form.id_proveedor.choices = [
        (proveedor["id_proveedor"], proveedor["nombre"])
        for proveedor in proveedores
    ]

    # Registrar producto
    if form.validate_on_submit():
        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO productos (
                nombre,
                categoria,
                precio,
                stock,
                id_proveedor
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            form.nombre.data,
            form.categoria.data,
            form.precio.data,
            form.stock.data,
            form.id_proveedor.data
        ))

        conn.commit()

        cursor.close()
        conn.close()

        flash("Producto registrado correctamente.", "success")
        return redirect(url_for("productos"))

    return render_template(
        "formulario_producto.html",
        nombre_sistema=nombre_sistema,
        form=form
    )

# Modificar producto

@app.route("/productos/editar/<int:id_producto>", methods=["GET", "POST"])
def editar_producto(id_producto):
    form = ProductoForm()

    # Cargar proveedores desde MySQL
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_proveedor, nombre
        FROM proveedores
        ORDER BY nombre
    """)

    proveedores = cursor.fetchall()

    cursor.close()
    conn.close()

    form.id_proveedor.choices = [
        (proveedor["id_proveedor"], proveedor["nombre"])
        for proveedor in proveedores
    ]

    # Cargar datos actuales del producto
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_producto,
            nombre,
            categoria,
            precio,
            stock,
            id_proveedor
        FROM productos
        WHERE id_producto = %s
    """, (id_producto,))

    producto = cursor.fetchone()

    cursor.close()
    conn.close()

    if producto is None:
        flash("El producto no existe.", "danger")
        return redirect(url_for("productos"))

    # Actualizar producto
    if form.validate_on_submit():
        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE productos
            SET
                nombre = %s,
                categoria = %s,
                precio = %s,
                stock = %s,
                id_proveedor = %s
            WHERE id_producto = %s
        """, (
            form.nombre.data,
            form.categoria.data,
            form.precio.data,
            form.stock.data,
            form.id_proveedor.data,
            id_producto
        ))

        conn.commit()

        cursor.close()
        conn.close()

        flash("Producto actualizado correctamente.", "success")
        return redirect(url_for("productos"))

    # Cargar datos actuales en el formulario
    if not form.is_submitted():
        form.nombre.data = producto["nombre"]
        form.categoria.data = producto["categoria"]
        form.precio.data = producto["precio"]
        form.stock.data = producto["stock"]
        form.id_proveedor.data = producto["id_proveedor"]

    return render_template(
    "formulario_producto.html",
    nombre_sistema=nombre_sistema,
    form=form,
    editar=True
)

# Eliminar producto

@app.route("/productos/eliminar/<int:id_producto>", methods=["POST"])
def eliminar_producto(id_producto):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM productos
        WHERE id_producto = %s
    """, (id_producto,))

    conn.commit()

    cursor.close()
    conn.close()

    flash("Producto eliminado correctamente.", "success")
    return redirect(url_for("productos"))


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
