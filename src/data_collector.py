# Step 1
# this function should find repos with cpp files and download them to temporary folder `data`
import requests
import os


# maybe we will need repeat 'gh auth login' in command line
def collect():
    # remove old data
    command = "rm -rf ../data && mkdir ../data && rm -rf ../input && mkdir ../input"
    os.system(command)

    repos = set()

    username = "eugenedar"
    token = ""
    url = 'https://api.github.com/search/repositories?q=language:cpp&page:1&per_page=30'

    for page in range(1, 5):

        r = requests.get(url, auth=(username, token))

        for item in r.json()['items']:
            size = item['size']  # size in Kb
            if size > 5000:
                continue

            full_name = item['full_name']

            repos.add(full_name)

        url = r.links['next']['url']
        print(url)

    print('Repos count:', len(repos))
    for name in repos:
        command = "gh repo clone " + name + " ../data/" + name
        os.system(command)
