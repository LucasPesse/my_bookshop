from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lucaspesse:root@localhost/my_bookshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email remains as a unique string
    password = db.Column(db.String(120), nullable=False)
    email_verified = db.Column(db.Boolean, default=False)  # Renamed from email

    def __repr__(self):
        return f'<User {self.email}>'

with app.app_context():
    db.create_all()

@app.get("/books")
def get_books():
    return {
        "books": [
            {
                "id": "aOEaEAAAQBAJ",
                "title": 'Gatsby le Magnifique',
                "author": 'F. Scott Fitzgerald',
                "cover": '/covers/gatsby.jpg',
                "price": '10,99 €'
            },
            {
                "id": "-n4gCgAAQBAJ",
                "title": "Ne tirez pas sur l'oiseau moqueur",
                "author": 'Harper Lee',
                "cover": '/covers/mockingbird.jpg',
                "price": '12,99 €'
            },
            {
                "id": "BFZlEAAAQBAJ",
                "title": '1984',
                "author": 'George Orwell',
                "cover": '/covers/1984.jpg',
                "price": '14,99 €'
            },
            {
                "id": "Ox5zwsnOp8MC",
                "title": 'Orgueil et Préjugés',
                "author": 'Jane Austen',
                "cover": '/covers/pride.jpg',
                "price": '9,99 €'
            }
        ]
    }

@app.route("/book/<int:id>")
def get_a_book(id):
    return {"book_id": id}

if __name__ == '__main__':
    app.run(debug=True)
