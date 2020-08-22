import socket

conn = socket.socket()      #Socket object creation

conn.connect(("localhost",8091))   #request is being made
# Tcp Connection establishes
data = input("Enter a Message> ")

conn.send(data.encode(encoding='utf_8',errors='strict')) 