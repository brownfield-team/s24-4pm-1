import os
import re
from datetime import datetime

# Get the repository name from the GITHUB_REPOSITORY environment variable
repo_name = os.getenv("GITHUB_REPOSITORY").split("/")[-1]

# Regular expression to match the team pattern
pattern = r"[sfw]\d{2}-\dpm-\d"

# Find the team in the repository name
match = re.search(pattern, repo_name)

# Get the current time
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Check if the logs directory exists and create it if it doesn't
if not os.path.exists("logs"):
    os.makedirs("logs")

# Open the log file
with open(f"logs/{repo_name}_{now}.txt", "w") as f:
    if match:
        # If a team is found, write it to the log file and print it
        team = match.group()
        f.write(team)
        print(team)
    else:
        # If no team is found, write a default value to the log file and print it
        default_value = f"failed to find a team for the repository {repo_name}"
        f.write(default_value)
        print(default_value)