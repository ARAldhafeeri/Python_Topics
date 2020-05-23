import socket
socket.setdefaulttimeout(4)
s = socket.socket()
s.connect(("192.168.8.1",20))
ans = s.recv(1024)
for i in ans:
     print(i)
