from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['JWT_SECRET_KEY'] = 'S3cureJWTKey_2025!FlaskAuth'

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes import task_bp, main
    from app.auth import auth_bp

    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main)

    return app
