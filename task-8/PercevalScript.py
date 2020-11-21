from bs4 import BeautifulSoup
import requests, os, perceval
 
req = requests.get('https://github.com/amfoss')
soup = BeautifulSoup(req.text, 'html.parser')
tags = soup.find_all('span', attrs={"class": "repo"})

for tag in tags:
    repo_name = (tag.parent.text).strip() #has a newline character before the text
    repo_url = "https://github.com/amfoss/"+""+repo_name
    repo_url = 'perceval git --json-line'+" "+repo_url
    print(repo_name, repo_url)
    os.system(repo_url+'>> commits.json')
