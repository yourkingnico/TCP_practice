import os
import socket
import sys
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'YOUR_HOST'
port = 9999
conn = s.connect((host, port))

print("input file to find on server: \n")
while True:
    cmd = input()
    if cmd == 'quit':
        s.close()
        sys.exit()
    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        server_response = str(s.recv(1024), "utf-8")
        print(server_response, end="")

        # while len(server_response2) < 1:
        #     server_response2 = s.recv(1024)
        #     if len(server_response2) > 1:
        #         print("File received!")


s.close()

