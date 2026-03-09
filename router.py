import json
import time

def handle_route(method, path):
      #dynamic routes 
    if path.startswith("/user/"):
        user_id = path.split("/")[-1]
        body = f"<h1>User ID: {user_id}</h1>"
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