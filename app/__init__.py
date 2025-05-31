from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes import task_bp
    from app.auth import auth_bp

    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)

    return app
