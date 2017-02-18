from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import pigLatin

class S(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.set_headers()
        self.wfile.write("Hello Vicarious")

    def do_HEAD(self):
        self.set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # Gets the size of data
        post_data = self.rfile.read(content_length) # Gets the data itself
        translation = pigLatin.to_pig_latin(post_data) # Calling translator
        self.set_headers()
        self.wfile.write(translation)
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()