# Imports defaultdict, a special dictionary type that assigns a default value to keys that don’t yet exist.
from collections import defaultdict
from typing import Tuple

def calculate_rankings(matches: list) -> list:
    """Calculate the rankings of a series of matches

    Args:
        matches (list): List of matches

    Returns:
        list: rankins 
    """
    # A defaultdict is initialized to store the points for each team, defaulting to 0 for any team not already present.
    team_points = defaultdict(int)
    # Loops through each match in the list of matches.
    for match in matches:
        # Calls a helper function to extract team names and scores from the match string.
        team1, score1, team2, score2 = parse_match(match)
        # Ensures both teams are added to the team_points dictionary. If not already present, they are initialized with a score of 0.
        if team1 not in team_points:
            team_points[team1] = 0
        if team2 not in team_points:
            team_points[team2] = 0
        # Award points based on the match result:
        # Win: The winning team gets 3 points.
        # Loss: The losing team gets 0 points.
        # Draw: Both teams get 1 point each.
        if score1 > score2:
            team_points[team1] += 3
        elif score1 < score2:
            team_points[team2] += 3
        else:
            team_points[team1] += 1
            team_points[team2] += 1
    
    # Converts the dictionary into a list of tuples, each containing a team and its total points.
    # First by points in descending order (-x[1]). The (-) is the descending flag
    # If points are tied, sort alphabetically by team name (x[0]). This is the second criteria
    sorted_teams = sorted(team_points.items(), key=lambda x: (-x[1], x[0]))
    # Build the ranking table
    rankings = []
    rank = 1
    prev_points = None
    # Iterate over the sorted teams:
    # i: The index of the current team in the sorted list (starting at 1).
    # (team, points): The team name and its total points.
    for i, (team, points) in enumerate(sorted_teams, start=1):
        if points != prev_points:
            rank = i
        rank_str = f"{rank}. {team}, {points} pt" if points == 1 else f"{rank}. {team}, {points} pts"
        rankings.append(rank_str)
        prev_points = points
    
    return rankings

def parse_match(match: str) -> Tuple[str, int, str, int]:
    """Parses a match result line and returns team names and scores

    Args:
        match (str): _description_

    Returns:
        Tuple[str, int, str, int]: Team1, score team 1, team 2, score team 2
    """
    # split(", "): Splits the match string into two parts, one for each team.
    parts = match.split(", ")
    # rsplit(" ", 1): Extracts the team name and score by splitting at the last space.
    # rsplit: Splits the string starting from the right side.
    # " ": Specifies that the split happens at spaces.
    # 1: Limits the split to a single occurrence, ensuring only one split happens (even if there are multiple spaces).
    team1, score1 = parts[0].rsplit(" ", 1)
    team2, score2 = parts[1].rsplit(" ", 1)
    # int(score1), int(score2): Converts the scores from strings to integers.
    return team1, int(score1), team2, int(score2)

def extract_match_values(datatable_str: str) -> list:
    """ Extract values from feature file

    Args:
        datatable_str (str): _description_

    Returns:
        list: converted list of matches or rankings
    """
    # Remove leading/trailing whitespace and split by newlines
    datatable_str = datatable_str.strip()
    # Split the string by lines and then by the delimiter (|) to create rows
    # This code processes a string (datatable_str) that is structured in a tabular format, 
    # where rows are separated by newline characters (\n), and columns within each row are separated by the pipe (|) character. 
    # datatable_str.split('\n'):
    #       Splits the datatable_str into a list of rows based on the newline (\n) character.
    # List comprehension [row.split('|') for row in datatable_str.split('\n')]:
    #       Iterates over each row in the list of rows produced by split('\n').
    #       For each row, it splits the row string into a list of columns using row.split('|'), separating the values at each pipe (|).
    rows = [row.split('|') for row in datatable_str.split('\n')]

    matches = []
    for row in rows:
        # Skip empty rows and the header row
        if row and len(row) > 1:  # Ensure there are columns
            match = row[1].strip()  # Access the second column for the match data
            if match and match != 'match' and match != 'ranking':  # Avoid appending the header row
                matches.append(match)

    return matches


