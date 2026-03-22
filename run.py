import os
from dotenv import load_dotenv
from app import create_app, db

# Load environment variables from .env file
load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    # Initialize the database inside app context if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run the application
    # Note: Use Gunicorn in production by pointing to `run:app`
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000)),
        debug=app.config.get('DEBUG', False)
    )
