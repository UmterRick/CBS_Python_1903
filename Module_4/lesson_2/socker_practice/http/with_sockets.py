import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('www.google.com', 80))
connect_data = [
    'GET / HTTP/1.1',
    'Host: www.google.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]

request_content = '\n'.join(connect_data)
print("==== HTML REQUEST DATA ====")
print(request_content)
print("==== END OF DATA ====\n")

sock.send(request_content.encode())
response = b''
while True:
    result = sock.recv(1024*1024*2)
    print(result + b"\n\n")
    if not result:
        break
    response += result

print(response)