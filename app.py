from flask import Flask, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is the ROM server!'

@app.route('/list')
def list_folders():
    roms_dir = '/media/httpanimations/Roms'
    folders = [f for f in os.listdir(roms_dir) if os.path.isdir(os.path.join(roms_dir, f))]
    return ','.join(folders)

@app.route('/list/<folder>')
def list_files(folder):
    roms_dir = '/media/httpanimations/Roms'
    folder_path = os.path.join(roms_dir, folder)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return ','.join(files)

@app.route('/download/<folder>/<filename>')
def download_file(folder, filename):
    roms_dir = '/media/httpanimations/Roms'
    folder_path = os.path.join(roms_dir, folder)
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    # Get the host IP address and port
    host = '0.0.0.0'
    port = 80

    print(f"Server running at http://{host}:{port}/")
    app.run(debug=True, host=host, port=port)
