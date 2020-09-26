import eventlet
eventlet.monkey_patch()


from flask import Flask
from flask_socketio import SocketIO, emit, join_room


socketio = SocketIO()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('join')
def handle_join(json):
    join_room('main room')
    emit('joined')


@socketio.on('msg')
def handle_msg(json):
    emit('msg received', json)


if __name__ == '__main__':
        socketio.run(app)
