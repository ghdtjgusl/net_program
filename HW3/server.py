from socket import *
import re

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break

        expr = data.decode()

        if expr == 'q':
            break

        expr = expr.replace(' ', '')

        try:
            match = re.match(r'(-?\d+)([+\-*/])(-?\d+)', expr)

            if not match:
                rsp = 'Try again'
            else:
                num1 = int(match.group(1))
                op = match.group(2)
                num2 = int(match.group(3))

                if op == '+':
                    rsp = str(num1 + num2)
                elif op == '-':
                    rsp = str(num1 - num2)
                elif op == '*':
                    rsp = str(num1 * num2)
                elif op == '/':
                    if num2 == 0:
                        rsp = 'Cannot divide by zero'
                    else:
                        rsp = f'{num1 / num2:.1f}'
                else:
                    rsp = 'Try again'

        except:
            rsp = 'Try again'

        client.send(rsp.encode())

    client.close()