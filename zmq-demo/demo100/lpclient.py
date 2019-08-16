import zmq

REQUEST_RETRIES = 3  # 重试次数
SERVER_ENDPOINT = 'tcp://localhost:5555'


context = zmq.Context()

client = context.socket(zmq.REQ)
client.connect(SERVER_ENDPOINT)

poller = zmq.Poller()
poller.register(client, zmq.POLLIN)

retries_left = REQUEST_RETRIES
queue_request = 0
while retries_left:
    queue_request += 1
    request = str(queue_request).encode()
    print('request: %s' % request)
    client.send(request)

    except_reply = True
    while except_reply:

        socks = dict(poller.poll(2500))
        if socks.get(client) == zmq.POLLIN:
            msg = client.recv()
            if msg == request:
                print(msg)
                retries_left = REQUEST_RETRIES
                except_reply = False
            else:
                print('error')
        else:
            retries_left -= 1
            poller.unregister(client)
            client.close()
            if retries_left == 0:
                print('服务错误')
                break

            print('服务重连中...')
            client = context.socket(zmq.REQ)
            client.connect('tcp://localhost:5555')
            poller.register(client, zmq.POLLIN)
client.close()

context.term()
