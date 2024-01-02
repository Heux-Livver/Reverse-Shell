import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("127.0.0.1", 4444))

print(s.recv(2048).decode('utf-8'))

while True:
    shell = input("$")
    s.send(shell.encode('utf-8'))

    recv = s.recv(2048).decode('utf-8')
    print(recv)
