import argparse

## Defines arguments for variables
parser = argparse.ArgumentParser(description='GITLAB_GROUP: The ID from the top group within Gitlab // GITLAB_TOKEN: The token to run API against gitlab // ORG_ID: Your Snyk Organization ID // INTEGRATION_ID: Your Snyk Organization Gitlab Integration ID')
parser.add_argument("--gitlab_group")
parser.add_argument("--gitlab_token")
parser.add_argument("--org_id")
parser.add_argument("--integration_id")

args = parser.parse_args()
gitlab_group = args.gitlab_group
gitlab_token = args.gitlab_token
org_id = args.org_id
integration_id = args.integration_id

import requests
import json

## Gets Gitlab repo data
url = 'https://gitlab.com/api/v4/groups/'+f'{gitlab_group}'+'/projects?include_subgroups=true&per_page=999'
headers = {'PRIVATE-TOKEN': f'{gitlab_token}'}
r = requests.get(url, headers=headers)
data = r.json()

## Defines import file
fname = 'import-projects.json'

## Creates file with appropriate content
with open(fname, 'w') as outfile:
  outfile.write('{"targets": [')

## Loops through list to add repo information
for element in data:
    with open(fname, 'a') as outfile:
    	json.dump({"target": {"id": element['id'], "branch": element['default_branch']}, "orgId": f"{org_id}", "integrationId": f"{integration_id}"}, outfile)
    	outfile.write(',')

## Closes off file with appropriate JSON
with open(fname, 'ab') as outfile:
	outfile.seek(-1, 2)
	outfile.truncate()

with open(fname, 'a') as outfile:	
	outfile.write(']}')