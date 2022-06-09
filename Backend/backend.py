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

engine = create_engine(
    'mysql+pymysql://user:password@host:3600/database',
    echo=True
)
Session = sessionmaker(bind=engine)
session = Session()

db = sqlalchemy(app)

Jaeger = db.get_all(Pjesme_Jaeger)
Bambus = db.get_all(Pjesme_Bambus)
Voda = db.get_all(Pjesme_Voda)
Gin = db.get_all(Pjesme_Gin)
Travarica = db.get_all(Pjesme_Travarica)
Vodka = db.get_all(Pjesme_Vodka)
Jack = db.get_all(Pjesme_Jack)
Merlot = db.get_all(Pjesme_Merlot)
Stock = db.get_all(Pjesme_Stock)

@app.route('/getanje/<pice>', methods=['GET'])
def fetch(pice):
    if pice == "bambus":
            return Bambus.select().order_by(Bambus.ocjena.desc())
    elif pice == "jaeger":
            return Jaeger.select().order_by(Bambus.ocjena.desc())
    elif pice == "voda":
            return Voda.select().order_by(Bambus.ocjena.desc())
    elif pice == "gin":
            return Gin.select().order_by(Bambus.ocjena.desc())
    elif pice == "travarica":
            return Travarica.select().order_by(Bambus.ocjena.desc())
    elif pice == "vodka":
            return Vodka.select().order_by(Bambus.ocjena.desc())
    elif pice == "jack":
            return Jack.select().order_by(Bambus.ocjena.desc())    
    elif pice == "merlot":
            return Merlot.select().order_by(Bambus.ocjena.desc())
    elif pice == "stock":
            return Stock.select().order_by(Bambus.ocjena.desc())

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
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200




if __name__ == '__main__':
   app.run(host="0.0.0.0")
   
