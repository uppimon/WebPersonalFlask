from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Email

###############Formularios de WTForms##############
class loginForm(FlaskForm):
    email=EmailField('Correo', validators=[DataRequired(), Email()])
    password=PasswordField('Contraseña', validators=[DataRequired()])
    submit=SubmitField('Ingrese')

class RegisterForm(FlaskForm):
    name=StringField('Nombre')
    last_name=StringField('Apellidos')
    email=EmailField('Correo')
    password=PasswordField('Contraseña')
    phone=IntegerField('Telefono')
    is_married=RadioField('Estado Civil', choices=[('True', 'Casado'), ('False', 'Soltero' )])
    gander=SelectField('Genero', choices=[('male', 'Masculino'), ('famale', 'Femenino' ), ('other', 'otro')])
    submit=SubmitField('Registrar')