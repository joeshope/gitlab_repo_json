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

## Defines json content for file write
def create_json():
	all_content = []
	for key in data:
		content = dict() 

		target = dict()
		target['id'] = key['id']
		target['branch'] = key['default_branch']
		content['target'] = target

		content['orgId'] = f"{org_id}"
		content['integrationId'] = f"{integration_id}"

		all_content.append(content)
	return all_content

## Defines import file
fname = 'import-projects.json'

## Creates file with appropriate content
with open(fname, 'w') as outfile:
  outfile.write('{"targets":')

with open(fname, 'a') as outfile:
	json.dump(create_json(), outfile)

## Closes off file with appropriate JSON
with open(fname, 'ab') as outfile:
	outfile.seek(-1, 2)
	outfile.truncate()

with open(fname, 'a') as outfile:	
	outfile.write(']}')
