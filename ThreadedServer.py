import socket

ip_address = '127.0.0.1'
port_number = 65000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((ip_address, port_number))

server_socket.listen(2)

client_socket, address = server_socket.accept()

print("Got connection from the client.....{}".format(address))
msg = client_socket.recv(1024).decode()
while true:
    
    print (msg.encode())

client_socket.close()

server_socket.close()