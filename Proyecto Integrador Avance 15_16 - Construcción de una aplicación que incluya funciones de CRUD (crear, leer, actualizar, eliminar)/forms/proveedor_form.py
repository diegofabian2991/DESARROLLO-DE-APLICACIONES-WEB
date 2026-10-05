from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ProveedorForm(FlaskForm):
    nombre = StringField(
        "Nombre del proveedor",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=100, message="El nombre debe tener entre 3 y 100 caracteres.")
        ]
    )

    especialidad = StringField(
        "Especialidad",
        validators=[
            DataRequired(message="La especialidad es obligatoria."),
            Length(min=3, max=100, message="La especialidad debe tener entre 3 y 100 caracteres.")
        ]
    )

    email = EmailField(
        "Correo electrónico",
        validators=[
            DataRequired(message="El correo electrónico es obligatorio."),
            Email(message="Ingrese un correo electrónico válido.")
        ]
    )

    submit = SubmitField("Registrar proveedor")