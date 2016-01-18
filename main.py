from __future__ import print_function
import requests
import soldier
import argparse
import json
import sys
from getpass import getpass

URL = 'https://api.github.com/user/repos'

py2 = True if sys.version_info[0] == 2 else False


def create_readme():
    pass

def create_repo(remote_ssh, description):
    dir_name = soldier.run('pwd').output
    repo_name = dir_name.strip().split('/')[-1]

    body = {'name': repo_name}
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--ssh', help='Adds the ssh url for git remote (Optionial). Default is https', action='store_true', default=False)
    parser.add_argument('-d', '--description', help='Description for github repo (Optional)', default='')
    parser.add_argument('-r', '--readme', help='Create README.md for github repo (Optional)', default=False, action='store_true')

    args = parser.parse_args()

    description = args.description
    create_readme() if args.readme else None
    
    resp = create_repo(args.ssh, description)
    if resp == 201:
        print('Repository created successfully')
    else:
        print('Some Error Occured')
