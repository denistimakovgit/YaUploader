import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = os.path.basename(file_path)
        disk_file_path = "Python/"+filename #создаем ссылку на файл для ЯндексДиск
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        result = response.json()
        href = result.get("href")

        upload_file = requests.put(href, data=open(filename, 'rb'))
        upload_file.raise_for_status()
        if upload_file.status_code == 201:
            print('Succes')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '/Users/denistimakov/PycharmProjects/YaUploader/text1.txt'
    token = "..."
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)