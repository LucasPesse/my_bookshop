from flask import Flask
from routes.user import init_user_routes
from routes.books import init_books_route
from models import db
from database import Database

app = Flask(__name__)

# DB configuration
app.config.from_object(Database)

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Tables created successfully!")

# User routes
init_user_routes(app)

# Book routes
init_books_route(app)

# Launcher

if __name__ == '__main__':
    app.run(debug=True)
