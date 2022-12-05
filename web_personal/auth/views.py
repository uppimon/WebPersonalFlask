
  ############ Imports Flask & Python ############
from flask import render_template, Blueprint

################# Imports Forms ##################

from .forms import loginForm, RegisterForm

auth_blueprint= Blueprint('auth', __name__)

####### Rutas Login #######
@auth_blueprint.route('/login',  methods=['GET', 'POST'])
def login():
    form=loginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        return render_template('admin/index.html', email=email)
    
    return render_template('/auth/login.html', form=form)

@auth_blueprint.route('/register')
def register():
    form=RegisterForm()
    return render_template('/auth/register.html', form=form)