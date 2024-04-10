import socket
import time
import json

class Server():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 65431
        self.BUFFER = 1024
        self.running = True
        
    def setup_connection(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.  SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        self.start_time = time.time()
    
    
    def server_uptime(self):
        self.current_time = time.time()
        self.uptime = self.current_time - self.start_time
        self.data = {"Uptime in seconds" : round(self.uptime, 2)}
        self.json_data = json.dumps(self.data)
        return self.json_data
    
    def server_info(self):
        self.version = {"Version" : "1.1.0"}
        self.json_version = json.dumps(self.version)
        return self.json_version
    
    # def server_stop(self):        
    #     self.client_socket.close()
    #     self.server_socket.close()
    
    def server_stop(self):
        self.running = False
        
    def stop_client_conn(self):
        self.client_socket.close()
            
        
    def server_help(self):
        self.fnc_list = {"UPTIME" : "Server uptime", "INFO" : "Version number" , "STOP" : "Close the connection", "HELP" : "List of functions"}
        self.json_fnc_list = json.dumps(self.fnc_list)
        return self.json_fnc_list
     
    
    def handle_commands(self):        
        self.client_socket, self.adress = self.server_socket.accept()
        print(f"Connection from IP: {self.adress[0]}, port: {self.adress[1]}")        
        
        name = self.client_socket.recv(self.BUFFER).decode("utf-8")
        
        print(f"User name: {name}")
        
        msg = f"Hello {name} on my server with IP {self.adress[0]}".encode("utf-8")
        self.client_socket.send(msg)
        
        command = self.client_socket.recv(self.BUFFER).decode("utf-8")
        if command == 'help':
            self.client_socket.send(self.server_help().encode("utf-8"))
        while self.running:
            chosen_command = self.client_socket.recv(self.BUFFER).decode("utf-8").strip()
            
            if chosen_command == 'help':
                self.client_socket.send(self.server_help().encode("utf-8"))
            elif chosen_command == 'uptime':
                self.client_socket.send(self.server_uptime().encode("utf-8"))
            elif chosen_command == 'info':
                self.client_socket.send(self.server_info().encode("utf-8"))
            elif chosen_command == 'stop':
                self.client_socket.send("Stopping server...".encode("utf-8"))
                self.stop_client_conn()
                self.server_stop()
                break
           
           
        
        
        
one = Server()
one.setup_connection()

while one.running:    
    one.handle_commands()
     
one.server_socket.close()         
    