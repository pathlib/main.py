import socket
#ce code n,as pas été coder par une ia
serveur =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HOST = "123.0.0.1"
PORT = 5001
serveur.bind((HOST,PORT))
serveur.listen()
