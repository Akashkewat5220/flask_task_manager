from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()       # Initialize db here
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['JWT_SECRET_KEY'] = 'aS3cureR@nd0mStr1ng!'

    db.init_app(app)         # Use db after initializing it
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes import task_bp, main
    from app.auth import auth_bp

    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main)

    return app
