import os
import ast
import sys
import time
import asyncio
import aiohttp
from typing import List, Tuple

async def create_issue(session: aiohttp.ClientSession, url: str, headers: dict, issue_data: dict, title: str) -> Tuple[str, str] | None:
    """Creates a single GitHub issue asynchronously."""
    try:
        async with session.post(url, headers=headers, json=issue_data) as response:
            response.raise_for_status()

            # --- Rate Limit Handling ---
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 1))
            if remaining_requests == 0:
                reset_time = int(response.headers.get('X-RateLimit-Reset'))
                sleep_time = max(0, reset_time - time.time() + 1)  # Add 1 second buffer
                print(f"Rate limit reached. Waiting for {sleep_time} seconds.")
                await asyncio.sleep(sleep_time)
                # Retry the request
                async with session.post(url, headers=headers, json=issue_data) as response:
                  response.raise_for_status()


            issue_url = response.json().get("html_url")
            print(f"Issue '{title}' created successfully at {issue_url}.")
            return title, issue_url

    except aiohttp.ClientResponseError as e:
        print(f"Failed to create issue '{title}'. Error: {e}")
        return None

async def create_github_issues(issues: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    # Retrieve environment variables
    repo_owner = os.getenv("REPO_OWNER")
    repo_name = os.getenv("REPO_NAME")
    auth_token = os.getenv("AUTH_TOKEN")
    comment_id = os.getenv("COMMENT_ID")

    if not repo_owner or not repo_name or not auth_token:
        raise ValueError("Missing required environment variables.")

    # GitHub API URL for creating issues
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

    # Headers for authentication and API versioning
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    created_issues_info = []
    failed_issues = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for title, body in issues:
            issue_data = {
                "title": title,
                "body": body
            }
            tasks.append(create_issue(session, url, headers, issue_data, title))

        results = await asyncio.gather(*tasks)

        for result in results:
            if result:
                created_issues_info.append(result)
            else:
                #  failed_issues list is not needed as we update the comment in create_issue function
                pass

    # Update the original comment with the results
    comment_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/comments/{comment_id}"
    if created_issues_info:
        comment_body = "The following issues were created:\n" + "\n".join(
            f"{i+1}. [{title}]({url})" for i, (title, url) in enumerate(created_issues_info)
        )
    else:
        comment_body = "No issues were created."

    try:
        async with aiohttp.ClientSession() as session:
          async with session.patch(comment_url, headers=headers, json={"body": comment_body}) as response:
            response.raise_for_status()
    except aiohttp.ClientResponseError as e:
        print(f"Failed to update comment. Error: {e}")
        sys.exit(1)


    return created_issues_info

if __name__ == "__main__":
    # Retrieve issues from environment variable and parse
    issues_str = os.getenv("ISSUES")
    if issues_str:
        try:
            # Safely evaluate the string to a list of lists
            issues = ast.literal_eval(issues_str)
            if isinstance(issues, list) and all(isinstance(issue, list) and len(issue) == 2 and all(isinstance(item, str) for item in issue) for issue in issues):
                asyncio.run(create_github_issues(issues))
            else:
                raise ValueError("Issues list is not in the correct format. Expected a list of lists, where each inner list contains two strings: [[title1, body1], [title2, body2], ...]")
        except (SyntaxError, ValueError) as e:
            print(f"Error parsing issues: {e}")
            sys.exit(1)
    else:
        print("No issues provided.")
        sys.exit(1)
