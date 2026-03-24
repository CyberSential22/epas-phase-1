import os
from app import create_app

# The entry point for Vercel must be an object named 'app'
# We initialize it using the application factory pattern
app = create_app(os.getenv('FLASK_CONFIG', 'production'))

if __name__ == "__main__":
    app.run()
