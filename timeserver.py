from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import sys
import time


class TimeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404, 'File not found')
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<html><body>%s</body><html>' % (time.asctime()))
        return


class TimeServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == "__main__":

    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000

    server = TimeServer(('', port), TimeHandler)
    server.serve_forever()
