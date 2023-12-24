import http.server
import socketserver
import threading

HTTP_PORT = 8000

class SimpleHTTPResponseHandler(http.server.SimpleHTTPRequestHandler):
    """
    A SimpleHTTPRequestHandler with custom GET logic. This prevents 
    listing directory contents which are enabled in the default implementation.
    """
    def do_GET(self):
        """Just respond with 200"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

def http_listen():
    with socketserver.TCPServer(("", HTTP_PORT), SimpleHTTPResponseHandler) as httpd:
        print("serving at port", HTTP_PORT)
        httpd.serve_forever()

def http_listen_thread():
    """
    Start a background thread that listens on HTTP_PORT.
    """
    server_thread = threading.Thread(target=http_listen)
    server_thread.daemon = True
    server_thread.start()
