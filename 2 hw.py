import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str, path_to_file: str, filename: str):
        self.token = token
        self.path_to_file = path_to_file
        self.filename = filename

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': self.path_to_file, 'overwrite': 'True'}
        response_upload = requests.get(upload_url, headers=headers, params=params)
        res = response_upload.json().get("href", "")
        response_url = requests.put(res, data=open(self.filename, 'rb'))
        response_url.raise_for_status()
        if response_url.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'netology/test'
    filename = 'test_file.txt'
    token = ''
    uploader = YaUploader(token, path_to_file, filename)
    uploader.upload()