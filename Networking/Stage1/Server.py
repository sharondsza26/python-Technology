import socket

print("Starting the Socket")
ss = socket.socket()        #Server-Socket Object creation

ss.bind(("localhost",8091)) #binding to end-point ie IpAddress and Portnumber 
# It has only one parameter which is tupple. Tupple has Ip and Port

ss.listen(5)
# upto 5 simultaneous requests listen, 6th will be rejected

print("Waiting for client")
socket,add = ss.accept()       #Flow of control will get blocked till request is made.
# Client has to make request to start work
# return value of accept is getting split across socket and add

print("Connected to ",add)

data = socket.recv(1024)        #Blocked
# until 1024 bytes is received

print("Client sent -> ",data.decode())

ss.close()