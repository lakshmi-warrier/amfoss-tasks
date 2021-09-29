from bs4 import BeautifulSoup
import requests, os, perceval
 

for page in [1,2]: #iterate through two pages
    req = requests.get('https://github.com/amfoss?page='+str(page)) 

    soup = BeautifulSoup(req.text, 'html.parser')

    tags = soup.find_all('a', itemprop="name codeRepository")

    for tag in tags:
        repo_name = str(tag.get_text()).strip() #has a newline character before the text
        repo_name.replace("Archived", "") # Get rid of the term "archived"
        repo_url = "https://github.com/amfoss/"+""+repo_name
        repo_url = 'perceval git --json-line'+" "+repo_url

        #print(repo_name, repo_url)
        os.system(repo_url+'>> commits.json')
