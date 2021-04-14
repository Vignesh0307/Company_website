from flask import Flask, render_template, url_for, flash, redirect

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


# this app is imported in run.py for this app it will run this page 
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#This is the sqlite database for using that we can crete by declaring class using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# to know about the login 
login_manager = LoginManager(app)
# login_view is the flask url we are dealing with 
login_manager.login_view = 'login'
# style for the login message 
login_manager.login_message_category = 'info'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'vigneshjul98@gmail.com'
app.config['MAIL_PASSWORD'] = 'Engineer@0307'
mail = Mail(app)

from flaskblog import routes
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.models import User, Post

