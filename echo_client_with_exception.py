import socket

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(adress)

while True:
    msg = input("Message to send: ")
    try:
        bytesSent = s.send(msg.encode())
    except:
        print('connection closed')
        break

    print("{} bytes send" .format(bytesSent))

    try:
        data = s.recv(BUFSIZE)
    except:
        print('connection closed')
        break

    print("{} bytes send" .format(bytesSent))

    try:
        data = s.recv(BUFSIZE)
    except:
        print('connection closed')
        break

    if not data:
        break

    print("Received message: %s" % data.decode())

s.close()
