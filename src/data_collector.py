# Step 1
# this function should find repos with cpp files and download them to temporary folder `data`
import requests
import os


# maybe we will need repeat 'gh auth login' in command line
def collect():
    # remove old data
    command = "rm -rf /data && mkdir /data && rm -rf /input && mkdir /input"
    os.system(command)

    username = "eugenedar"
    token = open("repo/git_token.txt", "r").readline()
    url = 'https://api.github.com/search/repositories?q=language:cpp&page:1&per_page=30'

    for page in range(1, 15):

        r = requests.get(url, auth=(username, token))

        for item in r.json()['items']:
            size = item['size']  # size in Kb
            if size > 50000:
                continue

            clone_url = item['clone_url']
            full_name = item['full_name']

            command = "git clone " + clone_url + " /data/" + full_name
            os.system(command)

        url = r.links['next']['url']
        print(url)
