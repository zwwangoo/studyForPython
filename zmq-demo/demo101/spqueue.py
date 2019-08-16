import zmq
context = zmq.Context()

brokerfe = context.socket(zmq.ROUTER)
brokerfe.bind('tcp://*:5555')

brokerbe = context.socket(zmq.ROUTER)
brokerbe.bind('tcp://*:5556')

poller = zmq.Poller()
poller.register(brokerbe, zmq.POLLIN)

workers = []
while True:

    if workers:
        poller.register(brokerfe, zmq.POLLIN)
    try:
        socks = dict(poller.poll())
    except zmq.ZMQError:
        break

    if socks.get(brokerbe) == zmq.POLLIN:
        msg = brokerbe.recv_multipart()
        addr, msg = msg[0], msg[2:]
        workers.append(addr)
        if msg[-1] != b'READY':
            brokerfe.send_multipart(msg)
    elif socks.get(brokerfe) == zmq.POLLIN:
        msg = brokerfe.recv_multipart()
        brokerbe.send_multipart([workers.pop(), b''] + msg)

brokerbe.close()
brokerfe.close()
context.term()
