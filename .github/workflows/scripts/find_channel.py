# find_channel.py
import os

def find_channel(team):
    with open('.github/workflows/scripts/teams.txt', 'r') as f:
        for line in f:
            team_name, channel_number = line.strip().split(':')
            if team_name == team:
                return channel_number
    return ""

team = os.getenv("TEAM")
channel_number = find_channel(team)
print(channel_number)