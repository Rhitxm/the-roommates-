import requests


def get_github_data(name):
    url = f"https://api.github.com/users/{name}/repos"
    response = requests.get(url) #gets/returns a response object and stores it in response
    

    if response.status_code == 200:
        repositories = response.json() #converts the json to a list of dictionaires 
        filtered_repositories = []
        for repo in repositories:
            filtered_repo = {
                "name": repo["name"],
                "description": repo["description"] or "Description not found",
                "language": repo["language"] or "Language not specified",
                "url": repo["html_url"],
                "stars": repo["stargazers_count"]
            }
            filtered_repositories.append(filtered_repo)
        return filtered_repositories
    else:
            print(f"Failed to retrieve data {response.status_code}")