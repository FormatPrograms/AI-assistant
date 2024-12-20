# libraries
import socket
import ollama as oll


def gen(c):
	response = oll.chat(model='CLEOaiAAR', messages=[{'role': 'user', 'content': f"{test}"},])
	sent = response['message']['content']
	c.send(sent.encode())


def main():
	ip = socket.gethostname()
	port = 8773
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((ip, port))
	s.listen(5)
	print("listening...")
	c, addr = s.accept()
	print("connection established.")

	while True:
		global test
		test = c.recv(1024).decode()
		print(test)
		else:
			gen(c)

main()
