import os
import requests
from urllib.request import urlretrieve

url = "https://api.github.com/repos/{}/pulls?state=all&page={}&per_page=100"

repos = ["yaptide/ui", "yaptide/yaptide", "yaptide/converter", "yaptide/deploy", "yaptide/docs", "DataMedSci/pymchelper"]

users = ["Bogdan2423", "kacper1409", "lequ0n", "hendzeld"]

response = requests.get(url.format(repos[0], 0))

patches = []

for repo in repos:
    repo = repo.split("/")[1]
    os.mkdir(repo)

for repo in repos:
    page = 0
    while True:
        response = requests.get(url.format(repo, page))
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                break
            for pr in data:
                if pr["user"]["login"] in users:
                    number = pr["number"]
                    patch_url = pr["patch_url"]
                    urlretrieve(patch_url, "{}/{}.patch".format(repo.split("/")[1], number))
            page += 1
        else:
            print(response.json())
            break
