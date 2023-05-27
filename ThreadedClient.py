import socket

ip_address = '127.0.0.1'
port_number = 65000


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((ip_address, port_number))


msg = "Hello world"

print (msg)

client_socket.close()




