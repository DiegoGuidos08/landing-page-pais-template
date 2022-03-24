from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user import Contacto

class RegisterForm(FlaskForm):
    nombre = StringField(validators=[InputRequired(), Length(min=1, max=20)],
                         render_kw={"placeholder": 'nombre'})
    
    apellido = StringField(validators=[InputRequired(), Length(min=1, max=20)],
                         render_kw={"placeholder": 'apellido'})
    
    correo = StringField(validators=[InputRequired(), Length(min=1, max=30)],
                         render_kw={"placeholder": 'correo'})    
    
    mensaje = StringField(validators=[InputRequired(), Length(min=1, max=300)],
                         render_kw={"placeholder": 'comentario'}) 
    
    submit = SubmitField("register")


    
    