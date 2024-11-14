from .. import socketio
from flask_socketio import send, emit

@socketio.on('connect')
def handle_connect():
    print('Client connected!')

@socketio.on('docs_change')
def handle_docs_change(text):
    emit("docs_update", {"new_docs": text}, broadcast=True)
    