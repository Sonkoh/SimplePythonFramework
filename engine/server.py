import http.server
import socketserver
import mimetypes
import os
from typing import List
from urllib.parse import urlparse, parse_qs

default_options = {'PROJECT_NAME': 'Nombre del Proyecto', 'PROJECT_HOST': '', 'PROJECT_PORT': '8000'}


class Handler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, data={ 'routes': None, 'DEFAULT_404': False }, **kwargs):
        self.routes = data["routes"]
        self.DEFAULT_404 = data["DEFAULT_404"]
        super().__init__(*args, **kwargs)
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        for route in self.routes:
            if parsed_url.path == route["path"] and route["method"] == "GET":
                self.send_response(route["response_code"])
                for header in route["headers"]:
                    self.send_header(header[0], header[1])
                self.end_headers()
                self.wfile.write(str(route["response"](data=query_params)).encode('ascii'))
                return
            
        file_path = os.path.join('public', parsed_url.path.lstrip('/'))
        if os.path.exists(file_path) and parsed_url.path.lstrip('/') != "":
            file_path = file_path
            mime_type, encoding = mimetypes.guess_type(file_path)
            self.send_response(200)
            self.send_header('Content-type', mime_type if mime_type != None else 'text/html')
            self.send_header('application/x-my-custom-type', mime_type if mime_type != None else 'text/html')
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
            return
        if (self.DEFAULT_404):
            self.send_response(int(self.DEFAULT_404["status"]))
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(self.DEFAULT_404["response"](data=query_params)).encode('ascii'))

    def do_POST():
        for route in self.routes:
            if parsed_url.path == route["path"] and route["method"] == "POST":
                self.send_response(route["response_code"])
                for header in route["headers"]:
                    self.send_header(header[0], header[1])
                self.end_headers()
                self.wfile.write(str(route["response"](data=query_params)).encode('ascii'))
                return
    def do_PATCH():
        for route in self.routes:
            if parsed_url.path == route["path"] and route["method"] == "PATCH":
                self.send_response(route["response_code"])
                for header in route["headers"]:
                    self.send_header(header[0], header[1])
                self.end_headers()
                self.wfile.write(str(route["response"](data=query_params)).encode('ascii'))
                return
    def do_DELETE():
        for route in self.routes:
            if parsed_url.path == route["path"] and route["method"] == "DELETE":
                self.send_response(route["response_code"])
                for header in route["headers"]:
                    self.send_header(header[0], header[1])
                self.end_headers()
                self.wfile.write(str(route["response"](data=query_params)).encode('ascii'))
                return

class Server(socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

class WebServer:
    def __init__(self, options=default_options):
        for option in default_options:
            options[option] = options.get(option, default_options[option])
        self.options = {}
        self.DEFAULT_404_FUNC = False
        for option in options:
            self.routes: List[str] = []
            self.options[option] = options[option]
    def DEFAULT_404(self, status: int = 404):
        def decorator(func):
            def wrapper(*args, **kwargs):
                response = func(*args, **kwargs)
                return response
            self.DEFAULT_404_FUNC = {
                "response": func,
                "status": status
            }
            return wrapper
        return decorator

    def call(self, method, route, function):
        self.routes.append({
            'path': route,
            'method': method,
            'response_code': 200,
            'headers': [('Content-type', 'text/html')],
            'response': function
        })

    def GET(self, route_path: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                response = func(*args, **kwargs)
                return response
            self.call("GET", route_path, wrapper)
            return wrapper
        return decorator

    def POST(self, route_path: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                response = func(*args, **kwargs)
                return response
            self.call("POST", route_path, wrapper)
            return wrapper
        return decorator
        
    def PATCH(self, route_path: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                response = func(*args, **kwargs)
                return response
            self.call("PATCH", route_path, wrapper)
            return wrapper
        return decorator
        
    def DELETE(self, route_path: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                response = func(*args, **kwargs)
                return response
            self.call("DELETE", route_path, wrapper)
            return wrapper
        return decorator

    def listen(self):
        with Server((self.options["PROJECT_HOST"], int(self.options["PROJECT_PORT"])), lambda *args, **kwargs: Handler(*args, data={ 'routes': self.routes, 'DEFAULT_404': self.DEFAULT_404_FUNC }, **kwargs)) as httpd:
            print("serving at port:", self.options["PROJECT_PORT"])
            httpd.serve_forever()