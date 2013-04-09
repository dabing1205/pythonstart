import socket
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print tcpsocket, udpsocket