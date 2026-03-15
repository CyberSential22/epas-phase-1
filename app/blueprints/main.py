from flask import Blueprint, render_template, current_app

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """System Home Page."""
    current_app.logger.info('Accessing Index Page')
    return render_template('main/index.html', status="Operational")

@main_bp.route('/about')
def about():
    """Project Information Page."""
    return render_template('main/about.html')
