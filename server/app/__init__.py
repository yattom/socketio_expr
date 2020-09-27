import eventlet

eventlet.monkey_patch()

import logging
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio_args = {}
# socketio_args['logger'] = app.logger
# socketio_args['engineio_logger'] = app.logger
socketio_args['cors_allowed_origins'] = '*'
socketio = SocketIO()
socketio.init_app(app, **socketio_args)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('join')
def handle_join():
    app.logger.info('join')
    join_room('main room')
    emit('joined')


@socketio.on('msg')
def handle_msg(json):
    app.logger.info(f'msg timestamp={json["timestamp"]}, seq={json["sequence"]}')
    emit('msg received', json)


if __name__ == '__main__':
    socketio.run(app)
