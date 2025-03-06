import os
import requests
from typing import List, Tuple

def create_github_issues(issues: List[Tuple[str, str]]):
    repo_owner = os.getenv("REPO_OWNER")
    repo_name = os.getenv("REPO_NAME")
    auth_token = os.getenv("AUTH_TOKEN")

    if not repo_owner or not repo_name or not auth_token:
        raise ValueError("Missing required environment variables.")

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    for title, body in issues:
        issue_data = {
            "title": title,
            "body": body
        }
        response = requests.post(url, headers=headers, json=issue_data)

        if response.status_code == 201:
            print(f"Issue '{title}' created successfully.")
        else:
            print(f"Failed to create issue '{title}'. Status code: {response.status_code}, Response: {response.json()}")

if __name__ == "__main__":
    issues_str = os.getenv("ISSUES")
    issues = ast.literal_eval(issues_str)  # Safely evaluate the string to a list of tuples
    create_github_issues(issues)
