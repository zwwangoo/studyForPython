import zmq

context = zmq.Context()

publisher = context.socket(zmq.PUB)
publisher.bind('tcp://*:5561')

syncservice = context.socket(zmq.REP)
syncservice.bind('tcp://*:5562')

SUBCOUNT = 10

subscriber = 0

while subscriber < SUBCOUNT:
    s = syncservice.recv()
    subscriber += 1

    syncservice.send(b'')

for updata_nbr in range(1000000):
    publisher.send_string('Rhubarb')

publisher.send_string('END')

publisher.close()
syncservice.close()
context.term()
