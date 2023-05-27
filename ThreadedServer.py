import socket
import threading

ip_address = '127.0.0.1'
port_number = 65000

THREADS = []
CMD_INPUT = []
CMD_OUTPUT = []


def handle_connection(connection,address):
    msg = connection.recv(1024).decode()
    while msg !='quit':
        print (msg)
        connection.send(msg.encode())


def close_connection(connection):
    connection.close()



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port_number))
server_socket.listen(5)
while True:
    connection, address = server_socket.accept()
    t = threading.Thread(target=handle_connection,args=(connection,address))
    THREADS.append(t)
    t.start()




server_socket.bind((ip_address, port_number))

server_socket.listen(2)

client_socket, address = server_socket.accept()

print("Got connection from the client.....{}".format(address))
msg = client_socket.recv(1024).decode()

while true:
    print (msg.encode())

client_socket.close()

server_socket.close()