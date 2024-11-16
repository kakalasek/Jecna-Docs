from .. import socketio
from flask_socketio import emit
from flask import request

user_list = []

@socketio.on('connect')
def handle_conect():
    user_list.append(request.sid)
    emit("update_user_list", {"user_list": user_list}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    user_list.remove(request.sid)
    emit("update_user_list", {"user_list": user_list}, broadcast=True)

@socketio.on('docs_change')
def handle_docs_change(text):
    emit("docs_update", {"new_docs": text}, broadcast=True)

#@socketio.on('draw_cursor')
#def handle_draw_cursor(coords):
#    emit("draw_cursor", {"x": coords['x'], "y": coords['y']}, broadcast=True)