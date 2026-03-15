import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app.config import config
from app.utils.logger import setup_logger

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_name: str = None) -> Flask:
    """
    Application Factory Pattern.
    Initializes Flask app, extensions, and logs.
    """
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    # Setup Logging
    setup_logger(app)

    # Register Blueprints
    from app.blueprints.main import main_bp
    from app.blueprints.events import events_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(events_bp, url_prefix='/events')

    # Global Error Handlers
    from app.errors import register_error_handlers
    register_error_handlers(app)

    return app
