import socket

HOST = 'localhost'
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print (f"[+] Listening on port {PORT} ...")

client, address = server.accept()
print (f"[+] Connected to {address}")

while True:
	cmd_input = input("shell:~#> ")
	client.send(cmd_input.encode('utf-8'))
	print (client.recv(1024).decode('utf-8'))
