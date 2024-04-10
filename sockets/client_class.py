import socket


class Client():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 65431
        self.BUFFER = 1024
        self.running = True
        
    def setup_connection(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        
    def client_intro(self):
        name = input("Your name: ").encode("utf-8")

        self.client_socket.send(name)
        print(self.client_socket.recv(self.BUFFER).decode("utf-8"))

        while True:
            command = input("Enter HELP to see my functions: ").lower()
            if command == 'help':                
                break
            
        self.client_socket.send(command.encode("utf-8"))
        print(self.client_socket.recv(self.BUFFER).decode("utf-8"))
    
    def client_cmd(self):
        cmd_pool = ['info', 'uptime', 'stop', 'help']
        
        while True:                           
            chosen_command = input("Enter one command: ").lower()
            if chosen_command in cmd_pool:
                break
        self.client_socket.send(chosen_command.encode("utf-8"))
        print(self.client_socket.recv(self.BUFFER).decode("utf-8"))
        if chosen_command == 'stop':
            self.client_stop()
        
    def client_stop(self):
        self.running = False
      
            

first = Client()
first.setup_connection()
first.client_intro()

# while True:
#     first.client_cmd()
while first.running:
    first.client_cmd()
first.client_socket.close()


        


