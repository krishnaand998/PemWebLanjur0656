from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize app and database connection
app = Flask(__name__)

# Configuring MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://db0656_carlateron:e907a837672ff9071e39cd799622db77a76020e9@3k4np.h.filess.io:3305/db0656_carlateron'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
