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

let total = 0;

/* ===========================
   VALIDAR NOMBRE
=========================== */

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

/* ===========================
   VALIDAR DESCRIPCIÓN
=========================== */

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

/* ===========================
   VALIDAR CATEGORÍA
=========================== */

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

/* ===========================
   EVENTOS EN TIEMPO REAL
=========================== */

nombreInput.addEventListener("input", validarNombre);
nombreInput.addEventListener("blur", validarNombre);

descripcionInput.addEventListener("input", validarDescripcion);
descripcionInput.addEventListener("blur", validarDescripcion);

categoriaInput.addEventListener("change", validarCategoria);
categoriaInput.addEventListener("blur", validarCategoria);

/* ===========================
   ENVIAR FORMULARIO
=========================== */

formulario.addEventListener("submit", function (event) {

    event.preventDefault();

    const nombreValido = validarNombre();
    const descripcionValida = validarDescripcion();
    const categoriaValida = validarCategoria();

    if (!nombreValido || !descripcionValida || !categoriaValida) {

        mensaje.innerHTML =
            "<div class='alert alert-danger'>Corrija los errores antes de registrar.</div>";

        return;
    }

    mensaje.innerHTML =
        "<div class='alert alert-success'>Registro agregado correctamente.</div>";

    const card = document.createElement("div");

    card.className = "card bg-dark text-white p-3 mt-3";

    const titulo = document.createElement("h5");
    titulo.textContent = nombreInput.value;

    const texto = document.createElement("p");
    texto.textContent = descripcionInput.value;

    const tipo = document.createElement("p");
    tipo.innerHTML = "<strong>Categoría:</strong> " + categoriaInput.value;

    const boton = document.createElement("button");

    boton.textContent = "Eliminar";
    boton.className = "btn btn-danger";

    boton.addEventListener("click", function () {

        lista.removeChild(card);

        total--;

        contador.textContent = total;

    });

    card.appendChild(titulo);
    card.appendChild(texto);
    card.appendChild(tipo);
    card.appendChild(boton);

    lista.appendChild(card);

    total++;

    contador.textContent = total;

    formulario.reset();

    nombreInput.classList.remove("is-valid");
    descripcionInput.classList.remove("is-valid");
    categoriaInput.classList.remove("is-valid");

    errorNombre.textContent = "";
    errorDescripcion.textContent = "";
    errorCategoria.textContent = "";
});