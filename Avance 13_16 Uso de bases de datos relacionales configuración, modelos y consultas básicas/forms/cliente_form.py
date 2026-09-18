from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ClienteForm(FlaskForm):
    nombre = StringField(
        "Nombre del cliente",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=100, message="El nombre debe tener entre 3 y 100 caracteres.")
        ]
    )

    sector = StringField(
        "Sector",
        validators=[
            DataRequired(message="El sector es obligatorio."),
            Length(min=3, max=80, message="El sector debe tener entre 3 y 80 caracteres.")
        ]
    )

    email = EmailField(
        "Correo electrónico",
        validators=[
            DataRequired(message="El correo electrónico es obligatorio."),
            Email(message="Ingrese un correo electrónico válido.")
        ]
    )

    submit = SubmitField("Registrar cliente")