import socket
import urllib


def backendServer():
    HOST = socket.gethostname()
    PORT_NUM = 8192

    server_socket = socket.socket()
    server_socket.bind((HOST, PORT_NUM))  # bind host address and port together

    while True:
        # How many clients can the server listen to simultaneously?
        server_socket.listen(1)
        conn, address = server_socket.accept()  # Accept connection
        print("Connection from: " + str(address))
    
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Recived: request (" + data + ")") 
            if(data == "SITE STATS"):
                print("hey")
                opener = urllib.URLopener()
                print("hey")
                
                url = "https://s3.amazonaws.com/office-environment-spy-back-end-data/site_0.csv"
                print("hey")
                file = opener.open(url)
                print("hey")
                conn.send(file.read().replace('\n', '@SPECIAL@'))  # send data to the client
#                conn.send("Cats")  # send data to the client
                print("hey")
            else:
                data = "Error: recived unknown request (" + data + ")"
                conn.send(data.encode())

        conn.close()  # close the connection


if __name__ == '__main__':
    backendServer()

