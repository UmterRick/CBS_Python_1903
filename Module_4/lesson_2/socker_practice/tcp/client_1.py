import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sk)
print(type(sk))

# ADDRESS = HOST + PORT
# Local Device Address: "localhost" , "127.0.0.1", "0.0.0.0"
print("Send message to PORT 8888")
message_text = input("Message: ")
sk.connect(("localhost", 8888))
sk.send(message_text.encode())  # 5000, 5050, 8000, 8080, 8000, 9090
print("Message Sent")