from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Enum definitions
from enum import Enum

db = SQLAlchemy()

class StatusEnum(Enum):
    EN_ATTENTE = "En attente"
    PAYE = "Payé"
    EXPEDIE = "Expédié"
    LIVRE = "Livré"
    ANNULE = "Annulé"

class PaymentMethodEnum(Enum):
    CARTE_CREDIT = "Carte de crédit"
    PAYPAL = "PayPal"
    VIREMENT = "Virement bancaire"

# User model
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    newsletter = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "newsletter": self.newsletter
        }

# Shopcart model
class Shopcart(db.Model):
    __tablename__ = 'shopcart'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship('User', backref=db.backref('shopcarts', lazy=True))

    def __repr__(self):
        return f'<Shopcart {self.id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "content": self.content,
            "created_at": self.created_at
        }

# ShopcartItem model
class ShopcartItem(db.Model):
    __tablename__ = 'shopcart_item'

    id = db.Column(db.Integer, primary_key=True)
    shopcart_id = db.Column(db.Integer, db.ForeignKey('shopcart.id'), nullable=False)
    book_id = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    shopcart = db.relationship('Shopcart', backref=db.backref('items', lazy=True))

    def __repr__(self):
        return f'<ShopcartItem {self.book_id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "shopcart_id": self.shopcart_id,
            "book_id": self.book_id,
            "quantity": self.quantity
        }

# Command model
class Command(db.Model):
    __tablename__ = 'command'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Integer, db.ForeignKey('shopcart.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Enum(StatusEnum), default=StatusEnum.EN_ATTENTE)

    user = db.relationship('User', backref=db.backref('commands', lazy=True))
    shopcart = db.relationship('Shopcart', backref=db.backref('commands', lazy=True))

    def __repr__(self):
        return f'<Command {self.id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "content": self.content,
            "value": self.value,
            "date": self.date,
            "status": self.status.value
        }

# Payment model
class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    command_id = db.Column(db.Integer, db.ForeignKey('command.id'), nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.now)
    payment_method = db.Column(db.Enum(PaymentMethodEnum), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    command = db.relationship('Command', backref=db.backref('payments', lazy=True))

    def __repr__(self):
        return f'<Payment {self.id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "command_id": self.command_id,
            "payment_date": self.payment_date,
            "payment_method": self.payment_method.value,
            "amount": self.amount
        }
