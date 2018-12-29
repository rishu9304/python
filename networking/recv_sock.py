import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = socket.gethostname()
ip = socket.gethostbyname(ip)

port = 5522

sock.connect((ip,port))

while True:
	data = sock.recv(1024)
	print("server :",data.decode())
	data = input()
	sock.send(data.encode())