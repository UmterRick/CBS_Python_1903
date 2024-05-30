import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Create Socket")
sk.bind(('localhost', 8888))
sk.listen(5)
print("Bind Socket on PORT 8888")
sk.settimeout(3)
try:
    client, addr = sk.accept()
    print("Wait for any data ...")
    input_data = client.recv(1024)  # receive
    message = input_data.decode()
    print("Data received")
    print(f"Receive From({addr[0]}:{addr[1]})")
    print(f"Message: {message}")
    if message == "!exit":
        client.close()
        print("Socket closed")
except socket.error:
    print("No Connections")
except KeyboardInterrupt:
    sk.close()
    print("Socket closed")

