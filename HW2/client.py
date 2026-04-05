import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

sock.send("홍서현".encode())

student_id = sock.recv(1024)
print(student_id.decode())

sock.close()