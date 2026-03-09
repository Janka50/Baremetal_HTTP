import socket
from request_parser import parse_request
from file_handler import serve_file
from router import handle_route
import datetime
import threading

def log_request(method, path, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {method} {path} -> {status}")

def handle_client(client_socket):
    request_data = client_socket.recv(4096)

    if not request_data:
        client_socket.close()
        return

    request = request_data.decode()

    print("_____RAW REQUEST_____")
    print(request)

    parsed_request = parse_request(request)

    if not parsed_request:
        client_socket.close()
        return

    method = parsed_request["method"]
    path = parsed_request["path"]

    # 1️⃣ Try route handler first
    content, mime_type = handle_route(method, path)

    # 2️⃣ If no route → try static file
    if content is None:
        content, mime_type = serve_file(path)

    # 3️⃣ Build response
    if content is not None:
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += f"Content-Type: {mime_type}\r\n"
        response_headers += f"Content-Length: {len(content)}\r\n"
        response_headers += "\r\n"

        client_socket.sendall(response_headers.encode() + content)
        log_request(method, path, 200)
    else:
        body = "<h1>404 - File Not Found</h1>"
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(body)}\r\n"
        response += "\r\n"
        response += body

        client_socket.sendall(response.encode())
        log_request(method, path, 404)

    client_socket.close()



# SERVER LOOP

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_server.bind(("127.0.0.1", 8080))
socket_server.listen(5)

print("Server is listening on port 8080...")

while True:
    client_socket, addr = socket_server.accept()

    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()