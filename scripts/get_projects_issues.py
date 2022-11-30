"""
Use Github API to get the issues for hackathon projects for each hackathon.
Saves them to json files.

Your github token for the github API must be in a file called "token.txt"
in the same directory as this script.

"""
import json
from pathlib import Path

import requests
from utils import bhg_log
from utils import load_repositories_info
from utils import root_dir

USERNAME = "Remi-Gau"

log_level = "INFO"

log = bhg_log(name="bidspm")
log.setLevel(log_level)

with open(Path(__file__).parent.joinpath("token.txt")) as f:
    TOKEN = f.read().strip()


def get_gh_issues(gh_username, repo, auth_username=None, auth_token=None):

    issues = None

    log.info(f"\ngetting issues: {gh_username, repo}")

    url = f"https://api.github.com/repos/{gh_username}/{repo}/issues?per_page=200"
    log.info(url)

    auth = None
    if auth_username is not None and auth_token is not None:
        auth = (auth_username, auth_token)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        issues = response.json()
    else:
        log.error(f"Error {response.status_code}: {response.text}")

    return issues


def main():

    data_dir = root_dir().joinpath("data")

    repositories_info = load_repositories_info()

    for this_repo in repositories_info:

        gh_username = repositories_info[this_repo]["gh_username"]
        repository_name = repositories_info[this_repo]["repo"]
        issues = get_gh_issues(gh_username, repository_name, USERNAME, TOKEN)

        if issues is None:
            continue

        project_issues = []

        # only keep open issues that have the project label
        for this_issue in issues:

            if this_issue["state"] == "open":

                labels = [x["name"] for x in this_issue["labels"]]

                if any(
                    x in labels for x in repositories_info[this_repo]["project_label"]
                ):

                    log.debug(f"{this_issue['title']}")
                    log.debug(f"{labels}")

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
