
import json
import requests

TOKEN = 'ed207598f0a4772c8f0f7914fb4acbb901b0e3c8'

TASK_PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS', 'ITERATOR']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Deleted', 'Moved']

def prepare_headers():
    return {
        'Authorization':'token {}'.format(TOKEN),
        'Content-Type': "application/json",
        'Accept': "application/vnd.github.v3+json"
    }
def get_pulls(login = 'Seregacod', repos = 'python_au', state = 'open'):
    url = 'https://api.github.com/repos/' + login + '/' + repos + '/pulls?state=' + state
    all_pr = requests.get(url, headers = prepare_headers())
    return all_pr
def get_all_comms(pull):
    all_comms = requests.get(pull['commits_url'], headers = prepare_headers())
    return all_comms
def prepare_msg(name):
    print('Hello')
    check_res = []
    title = name.split()
    pref = title[0].split('-')
    if len(pref) == 1:
        pref.append('')
    elif len(pref) != 2:
        pref = ['','']

    task_pref, group = pref

    if task_pref not in TASK_PREFIX:
        check_res.append('Pull request title must star with {}'.format(TASK_PREFIX))
    if group not in GROUP:
        check_res.append('Pull request title must contain group {}'.format(GROUP))
    if len(title) < 2 or title[1] not in ACTION:
        check_res.append('Pull request title must start with {}'.format(ACTION))
    print(check_res)
    return '\n'.join(check_res)

def prep_body(pull, comment):
    return {
        'body':
            'Your PR title: {}\n Check results: \n{}'.format(pull['title'],comment),
        'path': requests.get(pull['url'] + '/files', headers = prepare_headers()).json()[0]['filename'],
        'position': 1,
        'commit_id': pull['head']['sha']
    }
def send_check_res_pr(pull, comment):
    if len(comment) > 0:
        r = requests.post(pull['url'] + '/comments', headers = prepare_headers(), data = json.dumps(prep_body(pull, comment)).encode("utf8"))
        print(r.json())

def check_pr(pull):
    print('Hello')
    message = prepare_msg(pull['title'])
    for commit in get_all_comms(pull).json():
        message = message + '\n' + prepare_msg(commit['commit']['message'])
        send_check_res_pr(pull, message)

def main():
    r = get_pulls('Seregacod', 'python_au', 'open')
    message = ''
    print(r)
    for pull in r.json():
        print(pull)
        check_pr(pull)

main()