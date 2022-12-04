from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

########### Rutas Public #########

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/portfolio')
def portfolio():
    projects = [ 
    {
            'name':'Primer proyecto',
            'description':'As we got further away, it [the Earth] diminished in size. Finally it shrank to the size of a marbie, the most beautiful you can imagine. The beutiful, warm...',
            'image':'img/home-bg.jpg',
            'url': 'https://www.google.com'
        },
        {
            'name':'Segundo proyecto',
            'description':'As we got further away, it [the Earth] diminished in size. Finally it shrank to the size of a marbie, the most beautiful you can imagine. The beutiful, warm...',
            'image':'img/about-bg.jpg',
            'url': 'https://www.xataka.com'
        },
        {
            'name':'Tercer Proyecto',
            'description':'As we got further away, it [the Earth] diminished in size. Finally it shrank to the size of a marbie, the most beautiful you can imagine. The beutiful, warm...',
            'image':'img/home-bg.jpg',
            'url': 'https://www.google.com'
        },
        {
            'name':'Cuartoo proyecto',
            'description':'As we got further away, it [the Earth] diminished in size. Finally it shrank to the size of a marbie, the most beautiful you can imagine. The beutiful, warm...',
            'image':'img/about-bg.jpg',
            'url': 'https://www.xataka.com'
        },
    ]
    return render_template('public/portfolio.html', projects=projects)
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

@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('errores/404.html'), 404

if __name__=='__main__':
    app.run(debug=True)