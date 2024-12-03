# Imports the sys module to handle command-line arguments, such as the input file.
import sys
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

def main(debug = False):
    """Main entry of the program to start

    Args:
        debug (bool, optional): To debug the program. Defaults to False.
    """
    if not debug:
        if len(sys.argv) < 2:
            print("Usage hint: python coding_test.py <input_file>")
            return
    
        input_file = sys.argv[1]
    else:
        input_file = "matches.txt"
    try:
        # input_file: The path to the file that will be opened (provided as a string).
        # 'r': Specifies that the file is being opened in read mode. This means the file's contents can be read but not modified.
        with open(input_file, 'r') as file:
            # Reads all lines from the file and stores them as a list of strings.
            # Each line in the file becomes a separate string in the list, and line breaks (\n) are preserved unless stripped later.
            matches = file.readlines()
        # This is a list comprehension that iterates over each match in the matches list.
        # The strip() method removes any leading or trailing whitespace (like spaces, newlines, or tabs) from each match string.
        # The result is a new list of cleaned strings representing the match results.
        rankings = calculate_rankings([match.strip() for match in matches])
        print("\n".join(rankings))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()