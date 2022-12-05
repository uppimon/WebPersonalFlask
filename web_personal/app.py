from flask import Flask

############### Importd de Apps Blueprint ####################
from home.views import home_blueprint
from auth.views import auth_blueprint
from error_pages.handlers import error_pages_blueprint



app = Flask(__name__)
app.config['SECRET_KEY']='secret'


############### Registro de Apps ####################
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(error_pages_blueprint)


if __name__=='__main__':
    app.run(debug=True)
