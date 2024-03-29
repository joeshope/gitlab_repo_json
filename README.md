# gitlab_repo_json
Creates a JSON in current directory for Step 4 of Snyk API Import Tool. The JSON contains all repository IDs from Groups and Subgroups as well as their default branch.

REQUIRED:

GITLAB_URL - This should match your gitlab URL for on-prem deployments or use https://gitlab.com otherwise.

GITLAB_GROUP_ID - This is available in the Gitlab UI or Gitlab API (https://docs.gitlab.com/ee/api/groups.html)

GITLAB_API_TOKEN - You’ll find this option in your user account settings area, in the Access Tokens section. Alternatively, a Group Access Token can be used to grant access to all projects within a GitLab group or subgroup, without contributing to GitLab's licensed user count.
https://gitlab.com/-/profile/personal_access_tokens
https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html

SNYK_ORGANIZATION_ID - You can find this at the top of the Organization Settings page on the Snyk UI (https://docs.snyk.io/user-and-group-management/structure-account-for-high-application-performance/manage-snyk-organizations) or using the API (https://snyk.docs.apiary.io/#reference/groups/list-all-organizations-in-a-group/list-all-organizations-in-a-group)

SNYK_ORGANIZATION_INTEGRATION_ID - You can find this at the bottom of the Gitlab Integration page on the Snyk UI (https://docs.snyk.io/integrations/git-repository-scm-integrations/gitlab-integration) or using the API (https://snyk.docs.apiary.io/#reference/integrations/integrations/list)


How to use:
- Clone repo
- Navigate into directory
- Run pip3 install -r requirements.txt
- Run using the above arguments

example: <pre><code>python3 generate_json.py --gitlab_url=https://gitlab.com --gitlab_group=GITLAB_GROUP_ID --gitlab_token=GITLAB_API_TOKEN  --org_id=SNYK_ORGANIZATION_ID --integration_id=SNYK_ORGANIZATION_INTEGRATION_ID</code></pre>

Save the import-projects.json file to use with the Snyk API Import Tool (https://github.com/snyk-tech-services/snyk-api-import)
