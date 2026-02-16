import socket
from request_parser import parse_request 

#create a TCP socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#prevent an address already in use error
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

socket_server.bind(('localhost', 8080))
socket_server.listen(1)
print('Server is listening on port 8080...')

#accept one connection and receive data
while True :
    client_socket, client_address = socket_server.accept() 
    request = client_socket.recv(1024).decode()

    print("_____RAW REQUEST_____")
    print(request)
    
    parsed_request = parse_request(request)

    if parsed_request:
      print(parsed_request)
    else:
      print("Invalid or empty request received")

   

    



    response = "HTTP/1.1 200 OK \r\n"
    response += "Content-Type: text/html \r\n"
    response += "Content-Length: 13 \r\n"
    response += "\r\n"
    response += "Hello, World!"

    client_socket.sendall(response.encode())



#closing connections

    client_socket.close()