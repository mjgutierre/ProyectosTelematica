from http.server import HTTPServer, BaseHTTPRequestHandler

HOST =""
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)#ok 
        self.send_header("content-type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello</h1></body></html>","utf-8")) #pass bytes encoded

    def do_POST(self):
        

server = HTTPServer((HOST,PORT), NeuralHTTP)
print("server now running...")

server.serve_forever()
server.server_close()
print("server stopped")