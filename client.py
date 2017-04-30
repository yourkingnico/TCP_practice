import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.0.0.89'
port = 9999
conn = s.connect((host, port))
request = True

while request:
    print("input file to find on server: \n")
    cmd = input()
    response = ""
    file = ''
    if cmd == 'quit':
        s.close()
        sys.exit()

    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        server_response = str(s.recv(1024), "utf-8")
        print(server_response, end="")
        request = False
    if not request:
            createFile = open("new_" + cmd, "wb")
            print("\n file created \n")
            while not request:
                print("true")
                data = s.recv(1024)
                print(str(data))
                createFile.write(data)
                if str(data) == "b''":
                    createFile.close()
                    request = True
                    s.close()
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    con = s.connect((host, port))


s.close()

