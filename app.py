import os
import sys

# Ensure the root directory is in the Python path for modular imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

# Vercel looks for the WSGI application object named `app` in the entrypoint
app = create_app(os.getenv('FLASK_CONFIG', 'default'))

if __name__ == '__main__':
    app.run()
