# BareMetal HTTP Server

A minimal HTTP web server built from scratch using Python sockets.

This project demonstrates how HTTP works internally — including request parsing, 
routing, static file serving, MIME handling, logging, and basic concurrency using threads.

## 🚀 Features

- TCP socket server (IPv4)
- Manual HTTP request parsing
- Static file serving (HTML, CSS, JS, images)
- Custom routing system
- Dynamic routes (e.g. `/user/123`)
- Query parameter parsing
- Proper HTTP response formatting
- Logging system
- Basic multithreading support
- Custom 404 handling

---

## 📂 Project Structure
baremetal-http/ │ ├── server.py          
# Main server entry point ├── router.py         
# Route handling logic ├── request_parser.py    
# HTTP request parser ├── file_handler.py     
# Static file serving │ └── public/           
# Static files ├── index.html 
├── style.css 
├── script.js
└── 404.html

---

## 🧰 Requirements

- Python 3.10+
- No external dependencies required


 ▶️ How to Run the Server

1. Clone the repository:

```bash
git clone <your-repo-url>
cd baremetal-http

#Starting the server

''python3 server.py''

#Open the browser and visit

''http://127.0.0.1:8080/''
