"""
Author: Samuel O Tijani
Client for a multi-client chat room.
"""
from socket import *

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print(server.recv(BUFSIZE))
name1 = input('Enter your name: ')
name = name1.encode()
server.send(name)

while True:
	record = server.recv(BUFSIZE)
	if not record:
		print('Server disconnected')
		break
	print(record)
	message1 = input('> ')
	message = message1.encode()
	if not message:
		print('Server disconnected')
		break
	server.send(message + '\n'.encode())
server.close()