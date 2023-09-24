from http.server import HTTPServer, BaseHTTPRequestHandler

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path = "index.html"
        try:
            with open(self.path) as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content_type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(content, "utf-8"))
        except Exception as error:
            print(error)

class ManageServer:
    def __str__(self, host="localhost", port='8080'):
        self.host = host
        self.port = port

    def run_server(self):
        httpd = HTTPServer((self.host, self.port), ServerHandler)
        print(f"Server is running at {self.host}:{self.port}")
        httpd.serve_forever()