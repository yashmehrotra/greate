import requests
import soldier
import json
import sys
from getpass import getpass

URL = 'https://api.github.com/user/repos'

py2 = True if sys.version_info[0] == 2 else False


def create_readme():
    pass

def create_repo(remote_ssh, description, name, is_private):
    if not name:
        dir_name = soldier.run('pwd').output
        repo_name = dir_name.strip().split('/')[-1]
    else:
        repo_name = name

    body = {
        'name': repo_name,
        'description': description,
        'private': is_private,
    }
    if py2:
        username = raw_input('Username: ')
    else:
        username = input('Username: ')
    password = getpass('Password: ')
    req = requests.post(URL, data=json.dumps(body), auth=(username, password))

    ssh_url = req.json()['ssh_url']
    https_url = req.json()['clone_url']
    
    remote_url = ssh_url if remote_ssh else https_url
    
    soldier.run('git init')
    soldier.run('git remote add origin {}'.format(remote_url))
    return req.status_code
