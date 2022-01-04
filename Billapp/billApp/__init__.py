from flask import Flask, app, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '01b33c44cdc0cc76a292ccc8'
db = SQLAlchemy(app)

from billApp import routes