'''
拓展请求-应答模式，使用broker进行负载均衡。

REQ(client)只需要和ROUTER对话;
REP(server)只需要和DEALER对话;

在请求-应答模式中使用到的四种套接字类型：

- DEALER是一种负载均衡，它会将消息分发给已连接的节点，并使用公平队列的机制处理接受到的消息。DEALER的作用就像是PUSH和PULL的结合。
- REQ发送消息时会在消息顶部插入一个空帧，接受时会将空帧移去。其实REQ是建立在DEALER之上的，但REQ只有当消息发送并接受到回应后才能继续运行。
- ROUTER在收到消息时会在顶部添加一个信封，标记消息来源。发送时会通过该信封决定哪个节点可以获取到该条消息。
- REP在收到消息时会将第一个空帧之前的所有信息保存起来，将原始信息传送给应用程序。在发送消息时，REP会用刚才保存的信息包裹应答消息。REP其实是建立在ROUTER之上的，但和REQ一样，必须完成接受和发送这两个动作后才能继续。
'''  # noqa
import zmq

context = zmq.Context()

brokerfe = context.socket(zmq.ROUTER)
brokerfe.bind('tcp://*:5560')

brokerbe = context.socket(zmq.DEALER)
brokerbe.bind('tcp://*:5561')

# 一个线程中如果有多个sokect,同时需要收发数据时,
# zmq提供polling sockets实现，
# 不用在send()或者recv()时阻塞socket
poller = zmq.Poller()
# POLLIN在recv()端，负责刷新recv端口，来接受信息
# POLLOUT在send()端口，负责刷新send端，来发送消息。
poller.register(brokerbe, zmq.POLLIN)
poller.register(brokerfe, zmq.POLLIN)

while True:
    # poller.poll()轮询
    socks = dict(poller.poll())
    if socks.get(brokerfe) == zmq.POLLIN:
        msg = brokerfe.recv_multipart()
        print('brokerfe', msg)
        brokerbe.send_multipart(msg)

    if socks.get(brokerbe) == zmq.POLLIN:
        msg = brokerbe.recv_multipart()
        print('brokerbe', msg)
        brokerfe.send_multipart(msg)
