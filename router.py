import json
import time

def handle_route(method, path):

    # homepage route
    if path == "/":
        body = "<h1>Welcome to BareMetal Server</h1>"
        return body.encode(), "text/html"

    # about page
    elif path == "/about":
        body = "<h1>About Page</h1><p>This is my custom HTTP server.</p>"
        return body.encode(), "text/html"

    # version endpoint
    elif path == "/version":
        data = {
            "server": "BareMetal HTTP",
            "version": "1.0"
        }
        return json.dumps(data).encode(), "application/json"

    # current time API
    elif path == "/api/time":
        data = {
            "time": time.ctime()
        }
        return json.dumps(data).encode(), "application/json"

    return None, None