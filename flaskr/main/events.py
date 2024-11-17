from .. import socketio
from flask_socketio import emit
from flask import request

user_list = []
cursors_list = []

@socketio.on('connect')
def handle_conect():
    user_list.append(request.sid)
    emit("update_user_list", {"user_list": user_list}, broadcast=True)
    cursors_list.append({'id': request.sid, "x": 0, "y": 0})
    emit("update_cursor_list", {"cursor_list": cursors_list}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    user_list.remove(request.sid)
    emit("update_user_list", {"user_list": user_list}, broadcast=True)
    for i in range(len(cursors_list)):
        if cursors_list[i]['id'] == request.sid:
            cursors_list.pop(i)
    emit("update_cursor_list", {"cursor_list": cursors_list}, broadcast=True)

@socketio.on('docs_change')
def handle_docs_change(text):
    emit("docs_update", {"new_docs": text}, broadcast=True)

@socketio.on('draw_cursor')
def handle_draw_cursor(coords):
    for i in range(len(cursors_list)):
        if cursors_list[i]["id"] == request.sid:
            cursors_list[i]['x'] = coords['x']
            cursors_list[i]['y'] = coords['y']
    emit("update_cursor_list", {"cursor_list": cursors_list}, broadcast=True)