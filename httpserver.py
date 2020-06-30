import http.server #py3
import socketserver
#used for seeing output of titles
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == 'server/':
            self.path = 'servers.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
handler_object = MyHttpRequestHandler
PORT = 8000
my_server = socketserver.TCPServer(("0.0.0.0", PORT), handler_object)
my_server.serve_forever()
