import requests

def create_pull_request(token, owner, repo, title, head, base, body=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "head": head,
        "base": base,
        "body": body
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("Pull request created successfully.")
        return response.json()
    else:
        print("Failed to create pull request:")
        print(response.text)
        return None

# Example usage
if __name__ == "__main__":
    token = "your_personal_access_token"
    owner = "your_username"
    repo = "your_repository"
    title = "Your Pull Request Title"
    head = "feature_branch"
    base = "main"
    body = "Description of your pull request"

    create_pull_request(token, owner, repo, title, head, base, body)
