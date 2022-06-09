from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import bson.json_util as json_util
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)
cors = CORS(app,resources = {r"/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABAZE_URI'] = 'mysql:///Databaza.db'

engine = create_engine('mysql+pymysql://root:password@host:3306/Databasa')
Base = declarative_base()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

db = sqlalchemy(app)

@app.route('/getanje/<pice>', methods=['GET'])
def fetch(pice):
    if pice == "bambus":
            Bambus = db.get_all(Pjesme_Bambus)
            return Bambus.select().order_by(Bambus.ocjena.desc())
    elif pice == "jaeger":
            Jaeger = db.get_all(Pjesme_Jaeger)
            return Jaeger.select().order_by(Jaeger.ocjena.desc())
    elif pice == "voda":
            Voda = db.get_all(Pjesme_Voda)
            return Voda.select().order_by(Voda.ocjena.desc())
    elif pice == "gin":
            Gin = db.get_all(Pjesme_Gin)
            return Gin.select().order_by(Gin.ocjena.desc())
    elif pice == "travarica":
            Travarica = db.get_all(Pjesme_Travarica)
            return Travarica.select().order_by(Travarica.ocjena.desc())
    elif pice == "vodka":
            Vodka = db.get_all(Pjesme_Vodka)
            return Vodka.select().order_by(Vodka.ocjena.desc())
    elif pice == "jack":
            Jack = db.get_all(Pjesme_Jack)
            return Jack.select().order_by(Jack.ocjena.desc())    
    elif pice == "merlot":
            Merlot = db.get_all(Pjesme_Merlot)
            return Merlot.select().order_by(Merlot.ocjena.desc())
    elif pice == "stock":
            Stock = db.get_all(Pjesme_Stock)
            return Stock.select().order_by(Stock.ocjena.desc())

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 200


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
   
