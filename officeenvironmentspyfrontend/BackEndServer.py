import socket


def backendServer():
    HOST = socket.gethostname()
    PORT_NUM = 8192

    server_socket = socket.socket()
    server_socket.bind((HOST, PORT_NUM))  # bind host address and port together

    # How many clients can the server listen to simultaneously?
    server_socket.listen(1)
    conn, address = server_socket.accept()  # Accept connection
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    backendServer()

