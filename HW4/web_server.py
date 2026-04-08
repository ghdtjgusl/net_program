from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80)) 
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    if not data:
        c.close()
        continue

    msg = data.decode()
    lines = msg.split('\r\n')
    if len(lines) > 0:
        req_line = lines[0].split(' ')
        if len(req_line) > 1:
            filename = req_line[1].strip('/')
            if filename == "": filename = "index.html"
            
            print(filename) 

    try:
        if filename == "index.html":
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html; charset=utf-8'
            content = f.read().encode('utf-8')
        elif filename == "iot.png":
            f = open(filename, 'rb')
            mimeType = 'image/png'
            content = f.read()
        elif filename == "favicon.ico":
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
            content = f.read()
        else:
            raise FileNotFoundError

        header = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
        c.send(header.encode())
        c.send(content)

    except FileNotFoundError:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        error_html = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        c.send(header.encode() + error_html.encode())

    c.close()