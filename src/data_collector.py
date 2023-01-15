# Step 1
# this function should find repos with cpp files and download them to temporary folder `data`
import requests
import os

def collect ():
    # remove old data
    command = "rm -rf ../data && mkdir ../data && rm -rf ../input && mkdir ../input"
    os.system(command)

    repos = list()

    username = "eugenedar"
    token = ""

    r = requests.get('https://api.github.com/search/repositories?q=language:cpp&per_page:500', auth=(username, token))

    for item in r.json()['items']:
        size = item['size']  # size in Kb
        if size > 50000:
            continue

        full_name = item['full_name']

        print("Name = ", full_name, "Size = ", size)

        # maybe we will need repeat 'gh auth login' in command line
        command = "gh repo clone " + full_name + " ../data/" + full_name
        # os.system(command)

        repos.append("../data/" + full_name)

    return repos