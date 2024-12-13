from flask import jsonify, request
from models import db, User

def init_user_routes(app):
    @app.get("/user/<string:mail>")
    def search_user(mail):
        user = db.session.execute(db.select(User).filter_by(email=mail)).scalar();
        return jsonify({
            "user_info": user.to_dict() if user else None
        })

    @app.get("/user/<int:id>")
    def get_user_by_id(id):
        user = db.session.execute(db.select(User).filter_by(id=id)).scalar();
        return jsonify({
            "user_info": user.to_dict() if user else None
        })

    @app.post("/api/user")
    def create_user():
        data = request.get_json()

        user = User(
            first_name=data["fname"],
            last_name=data["lname"],
            email=data["mail"],
            password=data["password"],
            newsletter=data["newsletter"]
        )

        db.session.add(user);
        db.session.commit();

        return {
            "status": 200,
            "id": user.id
        }

    @app.post("/api/auth/login")
    def login():
        info = request.get_json();
        mail = info["mail"];
        password = info["password"];

        account = db.session.execute(db.select(User).filter_by(email=mail, password=password)).scalar();

        return jsonify({
            "id": None if not account else account.id
        })

    @app.put("/api/user")
    def edit_user():
        data = request.get_json();

        id = data["id"];
        first_name = data["first_name"];
        last_name = data["last_name"];
        email = data["mail"];
        password = data["password"];
        newsletter = data["newsletter"];

        user = db.session.execute(db.select(User).filter_by(id=id)).scalar();
        user.first_name = first_name;
        user.last_name = last_name;
        user.email = email;
        user.newsletter = newsletter;

        if password != False:
            user.password = password;

        db.session.commit();

        return {
            "status": 200,
            "message": "Compte modifié avec succès"
        }
