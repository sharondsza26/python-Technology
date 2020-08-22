import socket

print("Starting the Socket")
ss = socket.socket()

ss.bind(("localhost",8091))

ss.listen(5)

print("Waiting for client")
socket,add = ss.accept()
print("Connected to ",add)

data = ""
while data != "q":
  data = socket.recv(1024).decode()
  print("Client sent -> ",data)

ss.close()