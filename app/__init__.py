from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask (__name__)
app.secret_key='ahsbfhjkagsfugwgf9w7r26826r32'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:% s@localhost/saleapp?charset=utf8mb4" % quote('Tandat25102003')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 6

db = SQLAlchemy(app)
login = LoginManager(app=app)