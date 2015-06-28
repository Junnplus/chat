import socket
port = 8081
host = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
BUFSIZE = 1024
msg = raw_input()
while msg:
    bytes_sent = s.sendto(msg[:BUFSIZE], (host, port))
    msg = msg[bytes_sent:]
