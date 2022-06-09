from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import bson.json_util as json_util
from sqlalchemy import create_engine
from models import *
from sqlalchemy.orm import sessionmaker,declarative_base

app = Flask(__name__)
cors = CORS(app,resources = {r"/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABAZE_URI'] = 'mysql:///Databaza.db'

engine = create_engine('mysql+pymysql://root:password@localhost/Databasa')
Base = declarative_base()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

db = SQLAlchemy(app)

class Bambus(db.Model):
    """Bambus pice"""
    __tablename__ = "bambus"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Jaeger(db.Model):
    """Jaeger pice"""
    __tablename__ = "jaeger"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Voda(db.Model):
    """Voda pice"""
    __tablename__ = "voda"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Gin(db.Model):
    """Gin pice"""
    __tablename__ = "gin"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Travarica(db.Model):
    """Travarica pice"""
    __tablename__ = "travarica"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Vodka(db.Model):
    """Vodka pice"""
    __tablename__ = "vodka"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Jack(db.Model):
    """Jack pice"""
    __tablename__ = "jack"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Merlot(db.Model):
    """Merlot pice"""
    __tablename__ = "merlot"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

class Stock(db.Model):
    """Stock pice"""
    __tablename__ = "stock"
    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    ime = db.Column(db.String(255), unique=True, nullable=False)
    ocjena = db.Column(db.Integer, nullable=False)
    url = db.Column(db.Text)

@app.route('/getanje/<pice>', methods=['GET'])
def fetch(pice):
    if pice == "bambus":
            Bambus = Bambus.query.all(Pjesme_Bambus)
            return Bambus.select().order_by(Bambus.ocjena.desc())
    elif pice == "jaeger":
            Jaeger = db.session.get_all(Pjesme_Jaeger)
            return Jaeger.select().order_by(Jaeger.ocjena.desc())
    elif pice == "voda":
            Voda = databaze.get_all(Pjesme_Voda)
            return Voda.select().order_by(Voda.ocjena.desc())
    elif pice == "gin":
            Gin = databaze.get_all(Pjesme_Gin)
            return Gin.select().order_by(Gin.ocjena.desc())
    elif pice == "travarica":
            Travarica = databaze.get_all(Pjesme_Travarica)
            return Travarica.select().order_by(Travarica.ocjena.desc())
    elif pice == "vodka":
            Vodka = databaze.get_all(Pjesme_Vodka)
            return Vodka.select().order_by(Vodka.ocjena.desc())
    elif pice == "jack":
            Jack = databaze.get_all(Pjesme_Jack)
            return Jack.select().order_by(Jack.ocjena.desc())    
    elif pice == "merlot":
            Merlot = databaze.get_all(Pjesme_Merlot)
            return Merlot.select().order_by(Merlot.ocjena.desc())
    elif pice == "stock":
            Stock = databaze.get_all(Pjesme_Stock)
            return Stock.select().order_by(Stock.ocjena.desc())

@app.route('/add', methods=['POST'])
def add():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   pice = data.pop("pice")
   data["ocjena"] = int(data["ocjena"])
   
   if pice == "Jaeger":
      Jaeger.insert_one(data)
   elif pice == "Bambus":
      Bambus.insert_one(data)
   elif pice == "Voda":
      Voda.insert_one(data)
   elif pice == "Gin":
      Gin.insert_one(data)
   elif pice == "Travarica":
      Travarica.insert_one(data)
   elif pice == "Vodka":
      Vodka.insert_one(data)
   elif pice == "Jack":
      Jack.insert_one(data)
   elif pice == "Merlot":
      Merlot.insert_one(data)
   elif pice == "Stock":
      Stock.insert_one(data)

@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200

@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    if (pice == "Bambus"):
      Bambus.update_many(myquery, newvalues)
    elif (pice == "Jaeger"):
      Jaeger.update_many(myquery, newvalues)
    elif (pice == "Voda"):
      Voda.update_many(myquery, newvalues)
    elif (pice == "Vodka"):
      Vodka.update_many(myquery, newvalues)
    elif (pice == "Stock"):
      Stock.update_many(myquery, newvalues)
    elif (pice == "Gin"):
      Gin.update_many(myquery, newvalues)
    elif (pice == "Travarica"):
      Travarica.update_many(myquery, newvalues)
    elif (pice == "Jack"):
      Jack.update_many(myquery, newvalues)
    elif (pice == "Merlot"):
      Merlot.update_many(myquery, newvalues)
    
if __name__ == '__main__':
   app.run(host="0.0.0.0")
   
