from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired


class FacturacionForm(FlaskForm):
    numero = StringField(
        "Número de factura",
        validators=[
            DataRequired(message="El número de factura es obligatorio."),
            Length(min=3, max=30, message="El número debe tener entre 3 y 30 caracteres.")
        ]
    )

    cliente = StringField(
        "Cliente",
        validators=[
            DataRequired(message="El cliente es obligatorio."),
            Length(min=3, max=100, message="El cliente debe tener entre 3 y 100 caracteres.")
        ]
    )

    total = FloatField(
        "Total",
        validators=[
            InputRequired(message="El total es obligatorio."),
            NumberRange(min=0.01, message="El total debe ser mayor que 0.")
        ]
    )

    estado = SelectField(
        "Estado",
        choices=[
            ("", "Seleccione un estado"),
            ("Pagada", "Pagada"),
            ("Pendiente", "Pendiente")
        ],
        validators=[
            DataRequired(message="Debe seleccionar un estado.")
        ]
    )

    submit = SubmitField("Registrar factura")