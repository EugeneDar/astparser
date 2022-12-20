# Step 1
# this function should find repos with cpp files and download them to temporary folder `data`
import requests
import os

def collect ():
    repos = list()

    username = "eugenedar"
    token = ""

    r = requests.get('https://api.github.com/search/repositories?q=language:cpp&per_page:100', auth=(username, token))

    for item in r.json()['items']:
        size = item['size']  # size in Kb
        if size > 3000:
            continue

        full_name = item['full_name']

        # maybe we will need repeat 'gh auth login' in command line
        command = "gh repo clone " + full_name + " ../data/" + full_name
        os.system(command)

        repos.append("../data/" + full_name)

    return repos