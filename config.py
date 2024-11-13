from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Initialize app and database connection
app = Flask(__name__)

# Configuring MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://37HHxmpeCD766gn.root:RjbCOFFow7IPy0e9@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
