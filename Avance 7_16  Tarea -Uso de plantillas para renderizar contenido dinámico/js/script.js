// ======================================================
// SMARTPREDICT AI
// DESARROLLO DE APLICACIONES WEB
// SEMANA 7
// ======================================================

// ===========================
// ELEMENTOS DEL DOM
// ===========================

const formulario = document.getElementById("formRegistro");

const lista = document.getElementById("listaRegistros");
const mensaje = document.getElementById("mensaje");
const contador = document.getElementById("contador");

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

// ===========================
// VALIDAR NOMBRE
// ===========================

function validarNombre() {

    if (nombreInput.value.trim() === "") {

        nombreInput.classList.add("is-invalid");
        nombreInput.classList.remove("is-valid");

        errorNombre.textContent = "El nombre es obligatorio.";
        errorNombre.className = "text-danger";

        return false;
    }

    if (nombreInput.value.trim().length < 3) {

        nombreInput.classList.add("is-invalid");
        nombreInput.classList.remove("is-valid");

        errorNombre.textContent = "Debe tener mínimo 3 caracteres.";
        errorNombre.className = "text-danger";

        return false;
    }

    nombreInput.classList.remove("is-invalid");
    nombreInput.classList.add("is-valid");

    errorNombre.textContent = "Nombre correcto.";
    errorNombre.className = "text-success";

    return true;
}

// ===========================
// VALIDAR DESCRIPCIÓN
// ===========================

function validarDescripcion() {

    if (descripcionInput.value.trim() === "") {

        descripcionInput.classList.add("is-invalid");
        descripcionInput.classList.remove("is-valid");

        errorDescripcion.textContent = "La descripción es obligatoria.";

        errorDescripcion.className = "text-danger";

        return false;
    }

    if (descripcionInput.value.trim().length < 10) {

        descripcionInput.classList.add("is-invalid");
        descripcionInput.classList.remove("is-valid");

        errorDescripcion.textContent = "Debe tener mínimo 10 caracteres.";

        errorDescripcion.className = "text-danger";

        return false;
    }

    descripcionInput.classList.remove("is-invalid");
    descripcionInput.classList.add("is-valid");

    errorDescripcion.textContent = "Descripción correcta.";

    errorDescripcion.className = "text-success";

    return true;
}

// ===========================
// VALIDAR CATEGORÍA
// ===========================

function validarCategoria() {

    if (categoriaInput.value === "") {

        categoriaInput.classList.add("is-invalid");
        categoriaInput.classList.remove("is-valid");

        errorCategoria.textContent = "Seleccione una categoría.";

        errorCategoria.className = "text-danger";

        return false;
    }

    categoriaInput.classList.remove("is-invalid");
    categoriaInput.classList.add("is-valid");

    errorCategoria.textContent = "Categoría correcta.";

    errorCategoria.className = "text-success";

    return true;
}

// ===========================
// EVENTOS
// ===========================

nombreInput.addEventListener("input", validarNombre);
nombreInput.addEventListener("blur", validarNombre);

descripcionInput.addEventListener("input", validarDescripcion);
descripcionInput.addEventListener("blur", validarDescripcion);

categoriaInput.addEventListener("change", validarCategoria);
categoriaInput.addEventListener("blur", validarCategoria);

// ======================================================
// RENDERIZAR REGISTROS DINÁMICAMENTE
// ======================================================

function renderizarRegistros() {

    lista.innerHTML = "";

    // Condición cuando no existen registros
    if (registros.length === 0) {

        lista.innerHTML = `
            <div class="alert alert-warning">
                No existen registros disponibles.
            </div>
        `;

        contador.textContent = "0";
        return;
    }

    // Estructura repetitiva
    registros.forEach(function (registro, indice) {

        let colorEstado = "success";

        if (registro.estado === "Inactivo") {
            colorEstado = "danger";
        }

        const card = document.createElement("div");

        card.className = "card bg-dark text-white p-3 mt-3";

        card.innerHTML = `
            <h5>${registro.nombre}</h5>

            <p>${registro.descripcion}</p>

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

            <button class="btn btn-danger">
                Eliminar
            </button>
        `;

        card.querySelector("button").addEventListener("click", function () {

            registros.splice(indice, 1);

            mensaje.innerHTML = `
                <div class="alert alert-warning">
                    Registro eliminado correctamente.
                </div>
            `;

            renderizarRegistros();

        });

        lista.appendChild(card);

    });

    contador.textContent = registros.length;

}

// ======================================================
// ENVIAR FORMULARIO
// ======================================================

formulario.addEventListener("submit", function (event) {

    event.preventDefault();

    const nombreValido = validarNombre();
    const descripcionValida = validarDescripcion();
    const categoriaValida = validarCategoria();

    if (!nombreValido || !descripcionValida || !categoriaValida) {

        mensaje.innerHTML = `
            <div class="alert alert-danger">
                Corrija los errores antes de registrar.
            </div>
        `;

        return;
    }

    // Crear objeto

    const nuevoRegistro = {

        nombre: nombreInput.value,

        descripcion: descripcionInput.value,

        categoria: categoriaInput.value,

        estado: "Activo"

    };

    // Guardar en el arreglo


const spinner=document.getElementById("spinner");

spinner.classList.remove("d-none");


setTimeout(()=>{

spinner.classList.add("d-none");

},1000);


    registros.push(nuevoRegistro);

    mensaje.innerHTML = `
        <div class="alert alert-success">
            Registro agregado correctamente.
        </div>
    `;

    // Actualizar tarjetas

    renderizarRegistros();

    // Limpiar formulario

    formulario.reset();

    nombreInput.classList.remove("is-valid");
    descripcionInput.classList.remove("is-valid");
    categoriaInput.classList.remove("is-valid");

    errorNombre.textContent = "";
    errorDescripcion.textContent = "";
    errorCategoria.textContent = "";

});

// ======================================================
// CARGA INICIAL
// ======================================================

renderizarRegistros();