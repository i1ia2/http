import requests
import json
import pprint
respauns = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
hero_name = [{'name':'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
best_intelekt_name = []

def best():
    for here in respauns.json():
        for name in hero_name:
            if here['name'] == name['name']:
                best_intelekt_name = here['powerstats']['intelligence']
                print(best_intelekt_name)

print(best())


# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#
#         self.file_path = file
#         # Функция может ничего не возвращать
#

# if __name__ == '__main__':
#     path_to_file = ...
#     token = ...
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)




















