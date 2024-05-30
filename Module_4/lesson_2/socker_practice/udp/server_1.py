import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Create Socket")
sk.bind(('localhost', 8888))
print("Bind Socket on PORT 8888")
print("Wait for any data ...")
input_data = sk.recv(1024)  # receive
print("Data received")
print("Receive Message: ", input_data)
sk.close()
print("Socket closed")