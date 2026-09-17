// ======================================================
// SMARTPREDICT AI
// DESARROLLO DE APLICACIONES WEB
// SEMANA 7
// ======================================================

// ======================================================
// ELEMENTOS DEL DOM
// ======================================================

const formulario = document.getElementById("formRegistro");
const lista = document.getElementById("listaRegistros");
const mensaje = document.getElementById("mensaje");
const contador = document.getElementById("contador");

const spinnerCarga = document.getElementById("spinnerCarga");

let modalDetalle = null;

const elementoModal = document.getElementById("modalDetalle");

if (elementoModal && typeof bootstrap !== "undefined") {
    modalDetalle = new bootstrap.Modal(elementoModal);
}

const detalleNombre = document.getElementById("detalleNombre");
const detalleDescripcion = document.getElementById("detalleDescripcion");
const detalleCategoria = document.getElementById("detalleCategoria");
const detalleEstado = document.getElementById("detalleEstado");

const nombreInput = document.getElementById("nombre");
const descripcionInput = document.getElementById("descripcion");
const categoriaInput = document.getElementById("categoria");

const errorNombre = document.getElementById("errorNombre");
const errorDescripcion = document.getElementById("errorDescripcion");
const errorCategoria = document.getElementById("errorCategoria");

// ======================================================
// ARREGLO DE OBJETOS
// ======================================================

const registros = [

    {
        nombre: "Sensor IoT",
        descripcion: "Monitoreo inteligente de temperatura industrial.",
        categoria: "Sensor IoT",
        estado: "Activo"
    },

    {
        nombre: "PLC Siemens",
        descripcion: "Sistema de control para procesos automatizados.",
        categoria: "PLC",
        estado: "Activo"
    }

];

// ======================================================
// FUNCIONES DE VALIDACIÓN
// ======================================================

function validarNombre() {

    if (!nombreInput) {
        return false;
    }

    if (nombreInput.value.trim() === "") {

        nombreInput.classList.add("is-invalid");
        nombreInput.classList.remove("is-valid");

        if (errorNombre) {
            errorNombre.textContent = "El nombre es obligatorio.";
            errorNombre.className = "text-danger";
        }

        return false;
    }

    if (nombreInput.value.trim().length < 3) {

        nombreInput.classList.add("is-invalid");
        nombreInput.classList.remove("is-valid");

        if (errorNombre) {
            errorNombre.textContent = "Debe tener mínimo 3 caracteres.";
            errorNombre.className = "text-danger";
        }

        return false;
    }

    nombreInput.classList.remove("is-invalid");
    nombreInput.classList.add("is-valid");

    if (errorNombre) {
        errorNombre.textContent = "Nombre correcto.";
        errorNombre.className = "text-success";
    }

    return true;
}


// ======================================================
// VALIDAR DESCRIPCIÓN
// ======================================================

function validarDescripcion() {

    if (!descripcionInput) {
        return false;
    }

    if (descripcionInput.value.trim() === "") {

        descripcionInput.classList.add("is-invalid");
        descripcionInput.classList.remove("is-valid");

        if (errorDescripcion) {
            errorDescripcion.textContent = "La descripción es obligatoria.";
            errorDescripcion.className = "text-danger";
        }

        return false;
    }

    if (descripcionInput.value.trim().length < 10) {

        descripcionInput.classList.add("is-invalid");
        descripcionInput.classList.remove("is-valid");

        if (errorDescripcion) {
            errorDescripcion.textContent = "Debe tener mínimo 10 caracteres.";
            errorDescripcion.className = "text-danger";
        }

        return false;
    }

    descripcionInput.classList.remove("is-invalid");
    descripcionInput.classList.add("is-valid");

    if (errorDescripcion) {
        errorDescripcion.textContent = "Descripción correcta.";
        errorDescripcion.className = "text-success";
    }

    return true;
}


// ======================================================
// VALIDAR CATEGORÍA
// ======================================================

function validarCategoria() {

    if (!categoriaInput) {
        return false;
    }

    if (categoriaInput.value === "") {

        categoriaInput.classList.add("is-invalid");
        categoriaInput.classList.remove("is-valid");

        if (errorCategoria) {
            errorCategoria.textContent = "Seleccione una categoría.";
            errorCategoria.className = "text-danger";
        }

        return false;
    }

    categoriaInput.classList.remove("is-invalid");
    categoriaInput.classList.add("is-valid");

    if (errorCategoria) {
        errorCategoria.textContent = "Categoría correcta.";
        errorCategoria.className = "text-success";
    }

    return true;
}


// ======================================================
// MOSTRAR DETALLE EN MODAL
// ======================================================

function mostrarDetalle(registro) {

    if (!modalDetalle) {
        return;
    }

    if (detalleNombre) {
        detalleNombre.textContent = registro.nombre;
    }

    if (detalleDescripcion) {
        detalleDescripcion.textContent = registro.descripcion;
    }

    if (detalleCategoria) {
        detalleCategoria.textContent = registro.categoria;
    }

    if (detalleEstado) {
        detalleEstado.textContent = registro.estado;
    }

    modalDetalle.show();
}


// ======================================================
// EVENTOS DE VALIDACIÓN
// ======================================================

if (nombreInput) {

    nombreInput.addEventListener("input", validarNombre);
    nombreInput.addEventListener("blur", validarNombre);

}

if (descripcionInput) {

    descripcionInput.addEventListener("input", validarDescripcion);
    descripcionInput.addEventListener("blur", validarDescripcion);

}

if (categoriaInput) {

    categoriaInput.addEventListener("change", validarCategoria);
    categoriaInput.addEventListener("blur", validarCategoria);

}


// ======================================================
// RENDERIZAR REGISTROS DINÁMICAMENTE
// ======================================================

function renderizarRegistros() {

    // Si la página no tiene lista de registros,
    // no ejecutar esta función.
    if (!lista || !contador) {
        return;
    }

    lista.innerHTML = "";

    if (registros.length === 0) {

        lista.innerHTML = `
            <div class="alert alert-warning">
                No existen registros disponibles.
            </div>
        `;

        contador.textContent = "0";

        return;
    }

    registros.forEach(function (registro, indice) {

        let colorEstado = "success";

        if (registro.estado === "Inactivo") {
            colorEstado = "danger";
        }

        const card = document.createElement("div");

        card.className = "card bg-dark text-white shadow mt-3";

        card.innerHTML = `

            <div class="card-body">

                <h5 class="card-title">
                    ${registro.nombre}
                </h5>

                <p class="card-text">
                    ${registro.descripcion}
                </p>

                <p>
                    <strong>Categoría:</strong>
                    ${registro.categoria}
                </p>

                <p>
                    <strong>Estado:</strong>

                    <span class="badge bg-${colorEstado}">
                        ${registro.estado}
                    </span>
                </p>

                <button class="btn btn-info btn-sm btnDetalle">
                    <i class="bi bi-eye"></i>
                    Detalles
                </button>

                <button class="btn btn-danger btn-sm">
                    <i class="bi bi-trash"></i>
                    Eliminar
                </button>

            </div>
        `;


        // ==================================================
        // BOTÓN DETALLES
        // ==================================================

        const botonDetalle = card.querySelector(".btnDetalle");

        if (botonDetalle) {

            botonDetalle.addEventListener("click", function () {

                mostrarDetalle(registro);

            });

        }


        // ==================================================
        // BOTÓN ELIMINAR
        // ==================================================

        const botonEliminar = card.querySelector(".btn-danger");

        if (botonEliminar) {

            botonEliminar.addEventListener("click", function () {

                registros.splice(indice, 1);

                if (mensaje) {

                    mensaje.innerHTML = `
                        <div class="alert alert-warning">
                            Registro eliminado correctamente.
                        </div>
                    `;

                }

                renderizarRegistros();

            });

        }


        // Agregar tarjeta
        lista.appendChild(card);

    });


    // Actualizar contador
    contador.textContent = registros.length;

}


// ======================================================
// ENVIAR FORMULARIO
// ======================================================

if (formulario) {

    formulario.addEventListener("submit", function (event) {

        event.preventDefault();

        if (spinnerCarga) {
            spinnerCarga.classList.remove("d-none");
        }

        const nombreValido = validarNombre();
        const descripcionValida = validarDescripcion();
        const categoriaValida = validarCategoria();

        if (!nombreValido || !descripcionValida || !categoriaValida) {

            if (mensaje) {

                mensaje.innerHTML = `
                    <div class="alert alert-danger">
                        Corrija los errores antes de registrar.
                    </div>
                `;

            }

            if (spinnerCarga) {
                spinnerCarga.classList.add("d-none");
            }

            return;
        }


        // ==================================================
        // CREAR OBJETO
        // ==================================================

        const nuevoRegistro = {

            nombre: nombreInput.value,

            descripcion: descripcionInput.value,

            categoria: categoriaInput.value,

            estado: "Activo"

        };


        // ==================================================
        // GUARDAR REGISTRO
        // ==================================================

        registros.push(nuevoRegistro);


        if (mensaje) {

            mensaje.innerHTML = `
                <div class="alert alert-success">
                    Registro agregado correctamente.
                </div>
            `;

        }


        // Actualizar tarjetas
        renderizarRegistros();


        // Ocultar spinner
        setTimeout(function () {

            if (spinnerCarga) {
                spinnerCarga.classList.add("d-none");
            }

        }, 1000);


        // Limpiar formulario
        formulario.reset();

        nombreInput.classList.remove("is-valid");
        descripcionInput.classList.remove("is-valid");
        categoriaInput.classList.remove("is-valid");

        if (errorNombre) {
            errorNombre.textContent = "";
        }

        if (errorDescripcion) {
            errorDescripcion.textContent = "";
        }

        if (errorCategoria) {
            errorCategoria.textContent = "";
        }

    });

}


// ======================================================
// CARGA INICIAL
// ======================================================

renderizarRegistros();