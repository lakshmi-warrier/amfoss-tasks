import os
from github import Github

username = "amfoss"
g = Github()
user = g.get_organization(username)

for repo in user.get_repos():
    os.system(f"perceval git --json-line https://github.com/{repo.full_name} >> commits.json")
