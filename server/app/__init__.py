import eventlet
eventlet.monkey_patch()

import logging

from flask import Flask
from flask_socketio import SocketIO, emit, join_room


socketio = SocketIO()
logging.getLogger('socketio').setLevel(logging.ERROR)
logging.getLogger('engineio').setLevel(logging.ERROR)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('join')
def handle_join():
    app.logger.info('join')
    join_room('main room')
    emit('joined')


@socketio.on('msg')
def handle_msg(json):
    app.logger.info('msg')
    emit('msg received', json)


if __name__ == '__main__':
        socketio.run(app)
