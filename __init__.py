from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://udemy:udemy@localhost:3306/pyalmacen"
app.config.from_object('configuration.DevelopmentConfig')

db = SQLAlchemy(app)
#importar las vistas
from my_app.product.view import product

app.register_blueprint(product)

db.create_all()


#app.add_template_filter(iva_filter)

## Conexion con la base de datos ##

## Conexion con la base de datos ##

