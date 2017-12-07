#coding:utf-8
from flask import Flask,render_template
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask.ext.redis import FlaskRedis
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:950916@127.0.0.1:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']="57a9c928-06cf-4550-8d4c-0d7adf8a8250"
# app.config['REDIS_URL'] = "redis://localhost:6379/0"
app.config['REDIS_URL'] = "redis://192.168.3.23:6379/0"
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config['FACE_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/users/")
app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'),404