# Домашнее задание
from pprint import pprint
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {"path": file_path}
        headers = {"Authorization": token}
        # создаем папку с по полученым params = {"path": file_path}
        response = requests.put(url, headers=headers, params=params)
        url = url + '/upload'
        print(url)
        file_in_dir = os.listdir(file_path)
        # проходим циклом по списку]
        for file_i in file_in_dir:
            # собираем ссылку в полный путь к файлам
            file_full_path = file_path + '/' + file_i
            params = {"path": file_full_path}
            resp = requests.get(url, headers=headers, params=params)
            url_for_upload = resp.json().get('href', '')
            print(file_full_path)
            with open(file_full_path, 'rb') as file:
                response2 = requests.put(url_for_upload, files={"file": file})
            print(f'файл {url_for_upload} \n загружен!')
        # Функция может ничего не возвращать

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # убрать после проверки перед загрузкой в гит
    token = ''
    path_to_file = 'folder'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)