import os 

PUBLIC_DIR = "public"

def get_mime_type(path):
    if path.endswith('.html'):
        return "text/html"
    elif path.endswith('.css'):
        return "text/css"
    elif path.endswith('.js'):
        return "application/javascript"
    elif path.endswith('.png'):
        return "image/png"
    elif path.endswith('.txt'):
        return "text/plain"
    else:
        return "application/octet-stream"
    
    
def serve_file(path):
    if path == '/':
        path = '/index.html'
   
    if '..' in path:
        return None, None 
    file_path =path.lstrip('/')
    full_path = os.path.join(PUBLIC_DIR, file_path)
    print("Requested path:", path)
    print("Looking for file:", full_path)

    try:
        with open(full_path, "rb") as file:
            content = file.read()
            mime_type = get_mime_type(path)
            return content, mime_type
    except FileNotFoundError:
        return None, None