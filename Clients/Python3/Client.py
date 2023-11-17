import requests
import configparser

def read_base_url():
    config = configparser.ConfigParser()
    config.read('URL.ini')  # Assuming URL.ini is in the same directory as your script
    return config['DEFAULT']['base_url']

base_url = read_base_url()

def list_folders():
    try:
        response = requests.get(f'{base_url}/list')
        response.raise_for_status()
        folders = response.text.split(',')
        return folders
    except requests.exceptions.RequestException as e:
        print(f"Error listing folders: {e}")
        return []

def list_files(folder):
    try:
        response = requests.get(f'{base_url}/list/{folder}')
        response.raise_for_status()
        files = response.text.split(',')
        return files
    except requests.exceptions.RequestException as e:
        print(f"Error listing files in {folder}: {e}")
        return []

def download_file(folder, filename):
    try:
        url = f'{base_url}/download/{folder}/{filename}'
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)

        print('Download complete.')
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename} from {folder}: {e}")

if __name__ == '__main__':
    folders = list_folders()
    print('Folders:', folders)

    folder_name = input('Enter folder name to list files: ')
    files = list_files(folder_name)
    print('Files in', folder_name, ':', files)

    file_name = input('Enter filename to download: ')
    download_file(folder_name, file_name)
