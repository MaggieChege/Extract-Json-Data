from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Disposition(db.Model):
    __tablename__ = 'disposition'
    id = db.Column(db.Integer, primary_key=True)
    dispositionname = db.Column(db.Text, nullable=False, unique=True)


class DispositionSchema(ma.Schema):
    id = fields.Integer()
    dispositionname = fields.String()


class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    storename = db.Column(db.Text, nullable=False, unique=True)


class StoreSchema(ma.Schema):
    id = fields.Integer()
    storename = fields.String()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    calltype = db.Column(db.String(80))
    contacttype = db.Column(db.String(80))
    clientname = db.Column(db.Text, nullable=False)
    datecreated = db.Column(db.Text, nullable=False)
    disposition_id = db.Column(db.Integer, db.ForeignKey('disposition.id'), nullable=True)
    mobileno = db.Column(db.Text, nullable=False)
    questionsubtype = db.Column(db.Text, nullable=False)
    questiontype = db.Column(db.Text, nullable=False)
    sourcename = db.Column(db.Text, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=True)
    ticketid = db.Column(db.Integer, nullable=False)


class UsersSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    calltype = fields.String()
    contacttype = fields.String()
    clientname = fields.String()
    datecreated = fields.String()
    disposition_id = asset_id = fields.String()
    mobileno = fields.String()
    questionsubtype = fields.String()
    questiontype = fields.String()
    sourcename = fields.String()
    store_id = asset_id = fields.String()
    ticketid = db.Column(db.Integer)
