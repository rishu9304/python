import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = socket.gethostname()
ip = socket.gethostbyname(ip)

port = 5522

#binding the connection to the server
sock.bind((ip,port))

sock.listen(5)

conn,addr = sock.accept()

print("conn",conn)
print("sock",addr)

conn.send('connected to the server'.encode())

while True:
	data = conn.recv(1024)
	print("client :",data.decode())
	if not data:
		sock.close()
		print("connection aborted!!")
		break
	data = input()
	conn.send(data.encode())





#JNU-JPR/de/16/02/02/01303
