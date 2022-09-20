#задание 1
import requests
import json
import pprint
# respauns = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
# hero_name = [{'name':'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
# def best():
#     best_intelekt_name = []
#     for here in respauns.json():
#         for name in hero_name:
#             if here['name'] == name['name']:
#                 best_intelekt = here['powerstats']['intelligence']
#                 hero_int = (name['name'],best_intelekt)
#                 best_intelekt_name.append(hero_int)
#     return(f'самым умным героем является {sorted(best_intelekt_name, reverse=True)}')
# print(best())
# Задание 2
# token = ""

# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json',
#             'Authorization': f'OAuth {self.token}'
#         }
#
#     def get_files_list(self):
#         files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
#         headers = self.get_headers()
#         response = requests.get(files_url, headers=headers).json()
#         return response.json()
#
#     def upload(self, disk_file_path):
#         fail_url = "http://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = self.get_headers()
#         params = {'rath': disk_file_path, 'owerwrite': 'true'}
#         response = requests.get(fail_url, headers=headers, params=params)
#         pprint.pp(response.json())
#         return response.json()
#
#
#     def upload_file_to_disk(self, disk_file_path, filename):
#         href = self.upload(disk_file_path=disk_file_path).get("href", "")
#         response = requests.put(href, data=open(filename, 'rb'))
#         response.raise_for_status()
#         if response.status_code == 201:
#             print("Success")
#
# if __name__ == '__main__':
#

#     ya = YaUploader(token=token)
#     ya.upload_file_to_disk("disk", "fails.txt.txt")
#     pprint.pp(ya.get_files_list())
# Задание 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
                    'Content-Type': 'application/json',
                    'Authorization': f'OAuth {self.token}'
                }

    def upload(self, file_path: str):

        fail_url = "https://cloud-api.yandex.net//v1//disk//resources//upload"
        headers = self.get_headers()
        params = {'rath': file_path, 'owerwrite': 'true'}
        response = requests.get(fail_url, headers=headers, params=params)

        return response.json()

    def upload_file_to_disk(self, file_path, filename):
        href = self.upload(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    path_to_file = ('C://Users//Илюха//PycharmProjects//http//http//fails.txt')
    token = "y0_AgAAAABkQMeUAADLWwAAAADNsbZWSaN8cJTJSCe1NnKUopgdAFbz8nQ"
    yu = YaUploader(token)
    result = yu.upload(path_to_file)
    pprint.pp(result)
