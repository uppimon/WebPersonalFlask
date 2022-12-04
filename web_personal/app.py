from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Email
from home.views import home_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
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
####### Rutas Login #######

@app.route('/auth/login',  methods=['GET', 'POST'])
def login():
    form=loginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        return render_template('admin/index.html', email=email)
    
    return render_template('/auth/login.html', form=form)

@app.route('/auth/register')
def register():
    form=RegisterForm()
    return render_template('/auth/register.html', form=form)

@app.route('/welcome', methods=['GET', 'POST'])
def welcome(form):
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        return render_template('admin/index.html', email=email)
    
    return redirect(url_for('login'))

####### Apps ########


@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('error/404.html'), 404

app.register_blueprint(home_blueprint)

if __name__=='__main__':
    app.run(debug=True)