import requests
import json
from os import listdir
from os.path import isfile, join
import os


owner = "openstack"
repo = "nova"

#https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_commits(download_directory, token,since, page=1, per_page=2):
    query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        # "state": "open",
        # "author": "vishvananda",
        "per_page": per_page,
        "since": since,  # YYYY-MM-DDTHH:MM:SSZ
        "page": page
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.get(query_url, headers=headers, params=params)
    data = r.json()
    file_path = download_directory+str(page) + '.json'
    ensure_dir(file_path)
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
    return len(data)


def merge_json(file_path, directory="./"):
    file_names = sorted([f for f in listdir(directory) if isfile(join(directory, f))])
    commits = []
    for file_name in file_names:
        # Opening JSON file
        f = open(directory+file_name, )
        _commits = json.load(f)
        commits = commits + _commits
    ensure_dir(file_path)
    with open(file_path, 'w') as outfile:
        json.dump(commits, outfile)


def download_commits(token, since="2021-02-01", per_page=100, page=1, file_path='commits.json', download_directory="./"):
    length = get_commits(download_directory,token, since=since, page=page, per_page=per_page)
    page = page + 1
    while length == per_page:
        length = get_commits(download_directory,token,since="2021-02-01", page=page, per_page=per_page)
        page = page + 1
        print("Downloading...")
    merge_json(file_path, download_directory)


def read_commits(data_file_path):
    f = open(data_file_path, )
    commits = json.load(f)
    return commits
