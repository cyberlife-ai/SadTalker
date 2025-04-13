from flask import Flask
from flask_cors import CORS

def create_app():
    """Initialize the Flask app."""
    app = Flask(__name__)
    CORS(app)

    # Register routes
    from app.routes import sadtalker_routes
    app.register_blueprint(sadtalker_routes)

    return app