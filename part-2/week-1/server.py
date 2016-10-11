#!/usr/bin/python

# import socket module
import socket

# create socket
# IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ip and port number
my_ip = 'localhost'
my_port = 12345

# bind socket
s.bind((my_ip, my_port))
s.listen(5)
while True:
    print "Waiting for client ..."
    client, addr = s.accept()
    print "client is at ", addr
    data = client.recv(1024)
    if data:
        print "Message from client: %s" %data
    client.send("Thank you for your connection")
    client.close()
