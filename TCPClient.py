import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((socket.gethostname(),9090))
message = sock.recv(1024)
sock.close()
print(message.decode("ascii"))