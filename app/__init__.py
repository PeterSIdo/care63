from flask import Flask
from config import Config
from app.db_connection.conn import init_db_connection

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from app.main import bp as main_bp
    from app.login import bp as login_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)

    # Initialize database connection
    init_db_connection(app)

    return app