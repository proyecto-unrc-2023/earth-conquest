import os

from flask import jsonify, request
from app import create_app
from flask_socketio import SocketIO, emit

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
socketio = SocketIO(app,cors_allowed_origins="http://localhost:5173")

@app.route('/prueba-socket')
def prueba_socket():
    data = {'data':'prueba de web socket'}
    return jsonify(data)

@socketio.on('connect')
def handle_connect():
    print(request.sid)
    print('Cliente conectado')
    emit('connect', {
        'data':f'id:{request.sid} está conectado'
    })

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')
    emit('disconnect',f'user {request.sid} se desconecto', broadcast=True)

@socketio.on('message')
def handle_message(message):
    print(f'Mensaje recibido de frontend: {message}')
    emit('response', 'Respuesta desde el servidor', broadcast=True)

if __name__ == '__main__':
    print(app.url_map)
    # app.run(debug=True)
    socketio.run(app, debug=True)

