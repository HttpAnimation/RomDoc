from flask import Flask, send_from_directory, render_template, jsonify
from werkzeug.urls import url_quote
import os
import configparser

app = Flask(__name__)

# Function to read the ROMs path from the configuration file
def read_roms_path():
    config = configparser.ConfigParser()
    config.read('Path.ini')  # Assuming Path.ini is in the same directory as your script
    return config['DEFAULT']['roms_path']

# Use the function to get the ROMs path
roms_path = read_roms_path()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list_folders():
    try:
        folders = [f for f in os.listdir(roms_path) if os.path.isdir(os.path.join(roms_path, f))]
        return render_template('list.html', folders=folders)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/list/<folder>')
def list_files(folder):
    folder_path = os.path.join(roms_path, folder)
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return render_template('list.html', files=files, folder=folder)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<folder>/<filename>')
def download_file(folder, filename):
    folder_path = os.path.join(roms_path, folder)
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 80

    print(f"Server running at http://{host}:{port}/")
    app.run(debug=True, host=host, port=port)
