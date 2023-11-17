from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Specify the directory containing your ROMs
ROMS_DIR = "/media/httpanimations/Roms"

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROMS_DIR, **kwargs)

# Create an instance of the server
with TCPServer(("0.0.0.0", 80), MyHandler) as httpd:
    print("Server is running on port 80...")
    # Start the server
    httpd.serve_forever()
