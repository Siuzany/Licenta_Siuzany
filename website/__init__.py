from flask import flash, Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user, LoginManager
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask_mail import Mail
from config import Config



# app = Flask(__name__)
db = SQLAlchemy()

DB_NAME = "student.db"

mail = Mail()

def create_app():
    app = Flask(__name__)

    # app.secret_key= 'thiscode'

    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'Siuvccdff'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:siuzany2000$@localhost/DB_universitate'
    db.init_app(app)


# .........................
#     # Configurações do Mail
#     app.config['MAIL_SERVER'] = 'smtp.example.com'  # Substitua pelo servidor SMTP que deseja usar
#     app.config['MAIL_PORT'] = 587  # Substitua pelo porto do servidor SMTP
#     app.config['MAIL_USE_TLS'] = True
#     app.config['MAIL_USERNAME'] = 'seu_email@example.com'  # Substitua pelo seu endereço de email
#     app.config['MAIL_PASSWORD'] = 'sua_senha_de_email'  # Substitua pela senha do seu email

    # Importe as configurações do arquivo config.py
    # app.config.from_pyfile('config.py')
    mail = Mail(app)  # Crie a instância do Mail
    mail.init_app(app)
    app.config.from_object(Config)
    from .auth import auth  # Importe o blueprint "auth"
    from .views import views

    from .models import studentii


    # Registre o blueprint "auth"
    # app.register_blueprint(auth)



    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(ID):
        return studentii.query.get(int(ID))


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app