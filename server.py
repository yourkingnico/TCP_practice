import socket
import os


def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "/n" + "Retry...")
        socket_bind()


def socket_accept():
    #blocking
    conn, address = s.accept()
    print("Connection has been established | " + "IP: " + address[0] + " | Port: " + str(address[1]))
    get_commands(conn)


def get_commands(conn):
    while True:
        data = conn.recv(1024)

        if len(data) > 0:
            print("received, looking for: " + data[:].decode("utf-8") + " in " + str(os.getcwd()))
            found = False
            for file in os.listdir(str(os.getcwd())):
                if file == data[:].decode("utf-8"):
                    print("found the file!")
                    found = True
                    file_path = (os.path.abspath(file))
                    conn.send(str.encode("found " + data[:].decode("utf-8")))
                    readByte = open(file_path, "rb")
                    data = readByte.read()
                    readByte.close()
                    conn.send(data)
                    conn.close()
                    print("connection closed")
                    socket_accept()
            if not found:
                    print("File not Found")
                    conn.send(str.encode("-1"))


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
