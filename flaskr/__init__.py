from flask import Flask
import os
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='secret'
    )
    app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .main import main_page
    app.register_blueprint(main_page)

    socketio.init_app(app)
    return (app, socketio)