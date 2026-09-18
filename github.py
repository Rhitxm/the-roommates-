import requests


def get_repo_data(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url) #gets/returns a response object and stores it in response

    if response.status_code == 200: #response code 200 is , success/ok
        data = response.json()  #converts the json to a python object

        project = { #project is basically a filtered dictionary 
            "name": data["name"],
            "description": data["description"] or "Description not found", #or runs when data["desc"] returns None
            "language": data["language"] or "Language not specified",
            "url": data["html_url"],
            "stars": data["stargazers_count"]
        }

        return project

    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None
