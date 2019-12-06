import os
import logging
import requests
import time
from flask import Flask, request, jsonify
from multiprocessing import Process
from logger import log_init


procs = {}

log_init('Flask_Web')
app = Flask(__name__)
log = logging.getLogger()


def run_proc(name):
    res = requests.get('https://www.baidu.com')
    log.info(res.text)
    time.sleep(10)
    log.info(time.time())

    log.info('Run child process %s (%s)...' % (name, os.getpid()))


@app.route('/merck/remote/api/vidio/area', methods=['POST'])
def index():
    data = request.get_json()
    if not data:
        log.warning({'msg': 'parameter error.'})
        return jsonify({'msg': 'parameter error.'})

    cameraCode = data.get('cameraCode')
    if cameraCode in procs:
        procs[cameraCode].terminate()

    p = Process(target=run_proc, args=(cameraCode,))
    p.start()
    procs[cameraCode] = p

    return jsonify({
        'msg': 'Succ'
    })


if __name__ == '__main__':
    app.run()
