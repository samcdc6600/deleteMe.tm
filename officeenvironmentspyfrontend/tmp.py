import socket


HOST = "ec2-100-26-244-233.compute-1.amazonaws.com"
PORT_NUM = 8192

client_socket = socket.socket()
client_socket.connect((HOST, PORT_NUM))

request = "SITE STATS"

client_socket.send(request.encode())
data = client_socket.recv(1024).decode()

client_socket.close()
