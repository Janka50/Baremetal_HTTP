from urllib.parse import urlparse , parse_qs 

def parse_request(request_data):
    #split requests into lines
    lines = request_data.split("\r\n")
    if len(lines) == 0 or lines[0] == "":
        return None

    
    request_line = lines[0]
    
    parts = request_line.split(" ")

    if len(parts)<3:
        return None
    
    method = parts[0]
    raw_path = parts[1]
    version = parts [2]
    parsed_url = urlparse(raw_path)
    path = parsed_url.path
    query_params = parse_qs(parsed_url.query)
    #parse headers 
    headers = {}
    for line in lines:
        if line == "":
            break
        if  " :" in line :
            key , value = line.split (":" , 1)
            headers[key] = value 
            
    return {
        "method": method,
        "path": path,
        "version": version ,
        "headers": headers ,
        "query_params": query_params
        
    }
     