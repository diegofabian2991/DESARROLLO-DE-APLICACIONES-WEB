from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, InputRequired


class ProductoForm(FlaskForm):
    nombre = StringField(
        "Nombre del producto",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(
                min=3,
                max=100,
                message="El nombre debe tener entre 3 y 100 caracteres."
            )
        ]
    )

    categoria = SelectField(
        "Categoría",
        choices=[
            ("", "Seleccione una categoría"),
            ("Sensores", "Sensores"),
            ("Conectividad", "Conectividad"),
            ("Automatización", "Automatización"),
            ("Instrumentación", "Instrumentación")
        ],
        validators=[
            DataRequired(message="Debe seleccionar una categoría.")
        ]
    )

    precio = FloatField(
        "Precio",
        validators=[
            InputRequired(message="El precio es obligatorio."),
            NumberRange(
                min=0,
                message="El precio no puede ser negativo."
            )
        ]
    )

    stock = IntegerField(
        "Stock",
        validators=[
            InputRequired(message="El stock es obligatorio."),
            NumberRange(
                min=0,
                message="El stock no puede ser negativo."
            )
        ]
    )

    id_proveedor = SelectField(
        "Proveedor",
        coerce=int,
        validators=[
            DataRequired(message="Debe seleccionar un proveedor.")
        ]
    )

    submit = SubmitField("Registrar producto")