import socket

conn = socket.socket()

conn.connect(("localhost",8091))

# Infinite loop
while True:
  data = input("Enter a Message> ")
  conn.send(data.encode(encoding='utf_8',errors='strict'))