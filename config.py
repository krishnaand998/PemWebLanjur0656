from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize app and database connection
app = Flask(__name__)

# Configuring MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://krisdatabase_poetrythee:a3b75e70bf28a3654c989ddb682c83a9aa34b19e@5kyh4.h.filess.io:3307/krisdatabase_poetrythee'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
