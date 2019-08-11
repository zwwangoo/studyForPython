from flask import Flask, render_template
from flask_socketio import SocketIO
import random
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('test.html')


@socketio.on('connect', namespace='/test_conn')
def test_connect():
    t = random.randint(100, 10000)
    socketio.emit(
        'server_response',
        {'data': t},
        namespace='/test_conn',
    )


if __name__ == '__main__':
    socketio.run(app, debug=True)
