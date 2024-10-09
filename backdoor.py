import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("IP", 4444))

connection.send(b"[+] Connection Successful\n\n")

result = connection.recv(1024)
print(result)


connection.close()