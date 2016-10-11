#!/usr/bin/python

import socket

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ip and port number
my_ip = 'localhost'
my_port = 12347

dest_ip = 'localhost'
dest_port = 12345

# bind socket
s.bind((my_ip, my_port))

# connect to destination
s.connect((dest_ip, dest_port))

message = "Hello Mr. server I am from %s" %my_ip
s.send(message)
data = s.recv(1024)
print "Message from server: %s" %data
s.close()
