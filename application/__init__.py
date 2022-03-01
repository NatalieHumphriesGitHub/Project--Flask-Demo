from flask import Flask                                             #this file is so that it imports what we need from flask for the database
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                               #this is the name of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'         #this configures you to your local database - rather than the large SQL server - we will change this to connect for deployment - see notes on gsheet about connecting
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                #this says that we're not tracking modifications

db = SQLAlchemy(app)                                                #I think this is defining that the db is using SQLAlchmeny function with the parameter of the app

import application.routes                                           #this is importing the routes file from the application folder