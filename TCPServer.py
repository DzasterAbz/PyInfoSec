import socket

hostID = socket.gethostname()
portNO = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((hostID,portNO))
sock.listen(1)
print("\n Server Started! \n")

connection,address = sock.accept()
print("Connection Established with: ", str(address))
message = "\n Thank you for connecting "+str(address)
connection.send(message.encode("ascii"))
connection.close()