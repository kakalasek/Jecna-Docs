from .. import socketio
from flask_socketio import send, emit

@socketio.on('connect')
def handle_connect():
    print('Client connected!')

@socketio.on('docs_change')
def handle_docs_change(text):
    print(f"Docs text has changed: {text}")
    