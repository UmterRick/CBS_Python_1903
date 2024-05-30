import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Create Socket")
sk.bind(('localhost', 8888))
print("Bind Socket on PORT 8888")
while True:
    try:
        print("Wait for any data ...")
        input_data = sk.recv(1024)  # receive
        message = input_data.decode()
        print("Data received")
        print("Receive Message: ", message)
        if message == "!exit":
            sk.close()
            print("Socket closed")
            break
    except KeyboardInterrupt:
        sk.close()
        print("Socket closed")
        break


print("Server is shutting down!")