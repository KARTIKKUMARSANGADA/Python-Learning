import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))

server.listen(1)
print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected by", addr)

data = conn.recv(1024).decode()
print("Client says:", data)

conn.send("Hi".encode())

conn.close()
