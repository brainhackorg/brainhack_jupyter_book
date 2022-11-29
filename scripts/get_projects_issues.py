"""
Use Github API to get the issues for hackathon projects for each hackathon
Saves them to json files.
"""
import json
from pathlib import Path

import requests
from rich import print

USERNAME = "Remi-Gau"

with open(Path(__file__).parent.joinpath("token.txt")) as f:
    TOKEN = f.read().strip()

REPOSITORIES = {
    "ohbm_2019": {
        "owner": "ohbm",
        "repo": "hackathon2019",
        "project_label": ["Hackathon Project"],
    },
    "ohbm_2020": {
        "owner": "ohbm",
        "repo": "hackathon2020",
        "project_label": ["Hackathon project"],
    },
    "ohbm_2021": {
        "owner": "ohbm",
        "repo": "hackathon2021",
        "project_label": ["Atlantis", "Rising sun"],
    },
    "ohbm_2022": {
        "owner": "ohbm",
        "repo": "hackathon2022",
        "project_label": ["Hackathon Project"],
    },
    "brainhack_global_2020": {
        "owner": "brainhackorg",
        "repo": "global2020",
        "project_label": ["project"],
    },
    "brainhack_global_2021": {
        "owner": "brainhackorg",
        "repo": "global2021",
        "project_label": ["project"],
    },
    "brainhack_global_2022": {
        "owner": "brainhackorg",
        "repo": "global2022",
        "project_label": ["project"],
    },
}


def get_gh_issues(owner, repo, auth_username=None, auth_token=None):

    issues = None

    print(f"\n\n[red]getting issues: {owner, repo}[/red]")

    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    auth = None
    if auth_username is not None and auth_token is not None:
        auth = (auth_username, auth_token)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        issues = response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")

    return issues


def main():

    root_dir = Path(__file__).parents[1]

    data_dir = root_dir.joinpath("data")

    for this_repo in REPOSITORIES:

        owner = REPOSITORIES[this_repo]["owner"]
        repository_name = REPOSITORIES[this_repo]["repo"]
        issues = get_gh_issues(owner, repository_name, USERNAME, TOKEN)

        if issues is None:
            continue

        project_issues = []

        # only keep open issues that have the project label
        for this_issue in issues:

            if this_issue["state"] == "open":

                labels = [x["name"] for x in this_issue["labels"]]

                if any(x in labels for x in REPOSITORIES[this_repo]["project_label"]):

                    print(f"{this_issue['title']}")
                    print(f"{labels}")

                    project_issues.append(this_issue)

        output_file = data_dir.joinpath(f"projects_{this_repo}.json")
        with open(output_file, "w") as f:
            json.dump(project_issues, f, indent=4)


# issue keys
# ['url', 'repository_url', 'labels_url', 'comments_url', 'events_url', 'html_url', 'id', 'node_id',
# 'number', 'title', 'user', 'labels', 'state', 'locked', 'assignee', 'assignees', 'milestone', 'comments',
# 'created_at', 'updated_at', 'closed_at', 'author_association', 'active_lock_reason', 'body', 'reactions',
# 'timeline_url', 'performed_via_github_app', 'state_reason']

# labels keys
# ['id', 'node_id', 'url', 'name', 'color', 'default', 'description']

if __name__ == "__main__":
    main()
