import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app.config import config
from app.utils.logger import setup_logger
from werkzeug.middleware.proxy_fix import ProxyFix

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

    # Ensure SQLALCHEMY_DATABASE_URI is set before DB initialization
    # Priority: 1. Environment 'DATABASE_URL' 2. Existing config 3. Fallback to /tmp (Vercel writable)
    db_url = os.environ.get('DATABASE_URL') or app.config.get('SQLALCHEMY_DATABASE_URI')
    
    if not db_url:
        db_url = "sqlite:////tmp/epas.db"
    
    # Standardize postgresql:// if using external DB (e.g., Railway/Supabase)
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)

    # Initialize ProxyFix middleware conditionally
    if app.config.get('ENABLE_PROXY_FIX'):
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    with app.app_context():
        # Initialize database tables if they do not exist
        db.create_all()

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
