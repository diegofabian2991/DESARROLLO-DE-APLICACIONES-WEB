const formulario = document.getElementById("formRegistro");

const lista = document.getElementById("listaRegistros");

const mensaje = document.getElementById("mensaje");

const contador = document.getElementById("contador");

let total = 0;

formulario.addEventListener("submit", function(event){

    event.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();

    const descripcion = document.getElementById("descripcion").value.trim();

    const categoria = document.getElementById("categoria").value;

    if(nombre==="" || descripcion==="" || categoria===""){

        mensaje.innerHTML="<div class='alert alert-danger'>Todos los campos son obligatorios.</div>";

        return;
    }

    mensaje.innerHTML="<div class='alert alert-success'>Registro agregado correctamente.</div>";

    const card=document.createElement("div");

    card.className="card bg-dark text-white p-3 mt-3";

    const titulo=document.createElement("h5");

    titulo.textContent=nombre;

    const texto=document.createElement("p");

    texto.textContent=descripcion;

    const tipo=document.createElement("p");

    tipo.innerHTML="<strong>Categoría:</strong> "+categoria;

    const boton=document.createElement("button");

    boton.textContent="Eliminar";

    boton.className="btn btn-danger";

    boton.addEventListener("click",function(){

        lista.removeChild(card);

        total--;

        contador.textContent=total;

    });

    card.appendChild(titulo);

    card.appendChild(texto);

    card.appendChild(tipo);

    card.appendChild(boton);

    lista.appendChild(card);

    total++;

    contador.textContent=total;

    formulario.reset();

});