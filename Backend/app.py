from flask import Flask, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from sqlalchemy.orm import backref




app = Flask(__name__) # Name of app should be same as that of project name

CORS(app, resources={r"/*":{"origins":"*"}})

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['JWT_SECRET_KEY'] = 'super secret' #change this in real life (it should be some uid or secret string)


db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database Created')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database Dropped!')


@app.cli.command('db_seed')
def db_seed():

    dummy_user1 = User(card_token= 'kjadfji384709vihkjfoic9877',
                     budget=10000,
                     nobility_score=22,
                     name='Test User1',
                     email='test@test.com',
                     password='password',
                     address='56, xYZ STREET, Delhi, India')

    dummy_user2 = User(card_token= 'f978739478kdfjjkdhlck9e87r',
                     budget=4000,
                     nobility_score=0,
                     name='Test User2',
                     email='test2@test2.com',
                     password='test',
                     address='25, ABC STREET, Delhi, India')

    dummy_merchant1 = Merchant(merchant_id= 101,
                     name='ABC Shoe Emporium',
                     merchant_type='Footwear',
                     address='2, ABC STREET, India')

    dummy_merchant2 = Merchant(merchant_id= 512,
                     name='CCD',
                     merchant_type='Coffee',
                     address='12, Avenue STREET, Delhi ,India')

    dummy_merchant3 = Merchant(merchant_id= 652,
                     name='Safal',
                     merchant_type='Vegetable',
                     address='56, XYZ STREET, Delhi, India')
                     
    dummy_merchant4 = Merchant(merchant_id= 758,
                     name='Manish Book Store',
                     merchant_type='Stationary',
                     address='22, RT STREET, Delhi , India')

    dummy_merchant5 = Merchant(merchant_id= 489,
                     name='RANDOM RATION STORE',
                     merchant_type='Ration',
                     address='89, ABC STREET, Delhi , India')

    dummy_merchant6 = Merchant(merchant_id= 201,
                     name='XYZ Clothing store',
                     merchant_type='Clothing',
                     address='5, ABC STREET, India')

    dummy_merchant7 = Merchant(merchant_id= 732,
                     name='Mother Dairy',
                     merchant_type='Milk',
                     address='62, MG STREET, Delhi ,India')

    dummy_merchant8 = Merchant(merchant_id= 365,
                     name='Rajesh Juice Corner',
                     merchant_type='Juice Shop',
                     address='78, XYZ STREET, Delhi, India')
                     
    dummy_merchant9 = Merchant(merchant_id= 236,
                     name='McDonalds',
                     merchant_type='Pizza',
                     address='22, HR STREET, Delhi , India')

    dummy_merchant10 = Merchant(merchant_id= 912,
                     name='Burger King',
                     merchant_type='Burger',
                     address='79, ABC STREET, Delhi , India')  

    dummy_ngo1 = Ngo(ngo_id=485,
                    name = 'Milaap',
                    work_type='COVID Relief',
                    address='45, MG Street, Satya Niketan, Delhi, India')        

    dummy_ngo2 = Ngo(ngo_id=265,
                    name = 'Akshaya Patra',
                    work_type='Child Empowerment',
                    address='89, Sec 5, Dwarka, Delhi, India')  

    dummy_ngo3 = Ngo(ngo_id=894,
                    name = 'Goonj',
                    work_type='Women Empowerement',
                    address='45 Avenue, Green Park, Delhi, India')     

    dummy_ngo4 = Ngo(ngo_id=753,
                    name = 'Helpage India',
                    work_type='Old Age Support',
                    address='78, MN Street, Moti Bagh, Delhi, India')          
    
    dummy_ngo5 = Ngo(ngo_id=523,
                    name = 'United Way',
                    work_type='Support to Homeless',
                    address='12, Sec 10, RK Puram, Delhi, India')    

    
    dummy_transaction1 = Transaction(transaction_id=837409758497875,
                                    transaction_amount=2000,
                                    merchant_id=101,
                                    card_token='kjadfji384709vihkjfoic9877')    

    dummy_transaction2 = Transaction(transaction_id=557409758497875,
                                    transaction_amount=178,
                                    merchant_id=512,
                                    card_token='kjadfji384709vihkjfoic9877')  

    dummy_transaction3 = Transaction(transaction_id=787409758497865,
                                    transaction_amount=173,
                                    merchant_id=652,
                                    card_token='kjadfji384709vihkjfoic9877')  

    dummy_transaction4 = Transaction(transaction_id=712409758497875,
                                    transaction_amount=567,
                                    merchant_id=489,
                                    card_token='kjadfji384709vihkjfoic9877')  

    dummy_transaction5 = Transaction(transaction_id=264409758497875,
                                    transaction_amount=999,
                                    merchant_id=101,
                                    card_token='kjadfji384709vihkjfoic9877')  

    dummy_transaction6 = Transaction(transaction_id=56409758497875,
                                    transaction_amount=782,
                                    merchant_id=101,
                                    card_token='kjadfji384709vihkjfoic9877')     

    dummy_transaction7 = Transaction(transaction_id=432109758497875,
                                    transaction_amount=200,
                                    merchant_id=652,
                                    card_token='kjadfji384709vihkjfoic9877')  

    dummy_transaction8 = Transaction(transaction_id=118409758497875,
                                    transaction_amount=500,
                                    merchant_id=512,
                                    card_token='kjadfji384709vihkjfoic9877')  

    dummy_transaction9 = Transaction(transaction_id=654321758497875,
                                    transaction_amount=89,
                                    merchant_id=732,
                                    card_token='kjadfji384709vihkjfoic9877')  

    dummy_transaction10 = Transaction(transaction_id=123409758497875,
                                     transaction_amount=300,
                                     merchant_id=365,
                                     card_token='kjadfji384709vihkjfoic9877')  
                         
    dummy_donation1 = Donation(donation_id=8713546,
                               donation_amount=12,
                               ngo_id=485,
                               card_token='kjadfji384709vihkjfoic9877',
                               nobility_point_reward='5')  
    
    dummy_donation2 = Donation(donation_id=8713584,
                               donation_amount=20,
                               ngo_id=265,
                               card_token='kjadfji384709vihkjfoic9877',
                               nobility_point_reward='8')  
    
    dummy_donation3 = Donation(donation_id=8713632,
                               donation_amount=30,
                               ngo_id=753,
                               card_token='kjadfji384709vihkjfoic9877',
                               nobility_point_reward='9')  

    


    db.session.add(dummy_user1)
    db.session.add(dummy_user2)
    db.session.add(dummy_merchant1)
    db.session.add(dummy_merchant2)
    db.session.add(dummy_merchant3)
    db.session.add(dummy_merchant4)
    db.session.add(dummy_merchant5)
    db.session.add(dummy_merchant6)
    db.session.add(dummy_merchant7)
    db.session.add(dummy_merchant8)
    db.session.add(dummy_merchant9)
    db.session.add(dummy_merchant10)
    db.session.add(dummy_ngo1)
    db.session.add(dummy_ngo2)
    db.session.add(dummy_ngo3)
    db.session.add(dummy_ngo4)
    db.session.add(dummy_ngo5)
    
    db.session.add(dummy_transaction1)
    db.session.add(dummy_transaction2)
    db.session.add(dummy_transaction3)
    db.session.add(dummy_transaction4)
    db.session.add(dummy_transaction5)
    db.session.add(dummy_transaction6)
    db.session.add(dummy_transaction7)
    db.session.add(dummy_transaction8)
    db.session.add(dummy_transaction9)
    db.session.add(dummy_transaction10)

    db.session.add(dummy_donation1)
    db.session.add(dummy_donation2)
    db.session.add(dummy_donation3)
    
    db.session.commit()
    print('Database Seeded!')


@app.route('/')  # Root endpoint/url returning hello world .
def hello_world():
    return 'Index!'





@app.route('/register',methods=['POST'])
def register():
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='Email already registered!'), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify(message='Registration successful'), 201


@app.route('/login',methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']

    test = User.query.filter_by(email=email, password=password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message ='Login Successful!',access_token=access_token)
    else:
        return jsonify(message='Invalid credentials!'), 401


#database models
class User(db.Model):
    __tablename__ = 'users'
    card_token = Column(String,primary_key=True)
    budget = Column(Integer)
    nobility_score = Column(Integer)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)


class Userschema(ma.Schema):
    class Meta:
        fields=('card_token','budget','nobility_score' 'name', 'email', 'password', 'address')

class Merchant(db.Model):
    __tablename__ = 'merchants'
    merchant_id = Column(Integer,primary_key=True)
    name = Column(String)
    merchant_type = Column(String)
    address = Column(String)


class Merchantschema(ma.Schema):
    class Meta:
        fields=('merchant_id', 'name', 'merchant_type', 'address')

class Ngo(db.Model):
    __tablename__ = 'ngos'
    ngo_id = Column(Integer,primary_key=True)
    name = Column(String)
    work_type = Column(String)
    address = Column(String)


class Ngoschema(ma.Schema):
    class Meta:
        fields=('ngo_id', 'name', 'work_type', 'address')



class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer,primary_key=True)
    transaction_amount = Column(Integer)
    merchant_id = Column(Integer,ForeignKey('merchants.merchant_id'))
    merchants = relationship("Merchant", backref=backref("transactions", uselist=False))
    card_token = Column(String,ForeignKey('users.card_token'))
    users = relationship("User", backref=backref("transactions", uselist=False))


class Transactionschema(ma.Schema):
    class Meta:
        fields=('transaction_id', 'transaction_amount', 'merchant_id', 'card_token')

class Donation(db.Model):
    __tablename__ = 'donations'
    donation_id = Column(Integer,primary_key=True)
    donation_amount = Column(Integer)
    ngo_id = Column(Integer,ForeignKey('ngos.ngo_id'))
    ngos = relationship("Ngo", backref=backref("donations", uselist=False))
    card_token = Column(String,ForeignKey('users.card_token'))
    users = relationship("User", backref=backref("donations", uselist=False))
    nobility_point_reward = Column(Integer)


class Donationschema(ma.Schema):
    class Meta:
        fields=('donation_id', 'donation_amount', 'ngo_id', 'card_token','nobility_point_reward')


user_schema = Userschema()
users_schema = Userschema(many=True)

merchant_schema = Merchantschema()
merchants_schema = Merchantschema(many=True)

ngo_schema = Ngoschema()
ngos_schema = Ngoschema(many=True)

transaction_schema = Transactionschema()
transactions_schema = Transactionschema(many=True)

donation_schema = Donationschema()
donations_schema = Donationschema(many=True)


if __name__ == 'main':
    app.run()