import os

def find_channel(team):
    with open('.github/workflows/slack/teams.txt', 'r') as f:
        for line in f:
            team_name, channel_number = line.strip().split(':')
            print(f"Checking team: {team_name}")
            if team_name == team:
                print(f"Found team: {team_name}")
                return channel_number
    return ""

team = os.getenv("TEAM")
print(f"Team from environment: {team}")
channel_number = find_channel(team)
print(f"Channel number: {channel_number}")