import requests
import configparser

# Function to read the base URL from the configuration file
def read_base_url():
    config = configparser.ConfigParser()
    config.read('URL.ini')  # Assuming URL.ini is in the same directory as your script
    return config['DEFAULT']['base_url']

# Use the function to get the base URL
base_url = read_base_url()

def list_folders():
    response = requests.get(f'{base_url}/list')
    folders = response.text.split(',')
    return folders

def list_files(folder):
    response = requests.get(f'{base_url}/list/{folder}')
    files = response.text.split(',')
    return files

def download_file(folder, filename):
    url = f'{base_url}/download/{folder}/{filename}'
    response = requests.get(url, stream=True)
    
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

if __name__ == '__main__':
    folders = list_folders()
    print('Folders:', folders)

    folder_name = input('Enter folder name to list files: ')
    files = list_files(folder_name)
    print('Files in', folder_name, ':', files)

    file_name = input('Enter filename to download: ')
    download_file(folder_name, file_name)
    print('Download complete.')
