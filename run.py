from flaskr import create_app

if __name__ == "__main__":
    app, socketio = create_app()
    socketio.run(app, debug=True)