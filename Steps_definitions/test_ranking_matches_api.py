# test_ranking_matches.py
from pytest_bdd import scenarios, given, when, then, parsers
from utils import *


scenarios('ranking_matches.feature')

# Globals
matches = []
rankings = []
expected_results = []

# Scenario: Calculate rankings from a set of matches
# Scenario: Handle matches with tied rankings
# Scenario: Handle a single match
@given(parsers.parse('the following matches:{datatable}'))
def given_matches_list(datatable):
    global matches
    matches = extract_match_values(datatable)

@when("I calculate the rankings")
def calculate():
    global rankings
    rankings = calculate_rankings(matches)
    print(rankings)

@then(parsers.parse("the rankings should be:{expected_rankings}"))
def verify_rankings(expected_rankings):
    global expected_results 
    expected_results = extract_match_values(expected_rankings)
    print(rankings)
    assert rankings == expected_results, "The results does not macth"

# Scenario: Handle an empty list of matches
@given("no matches")
def given_no_matches():
    global matches
    matches = []
    print(matches)

@then("the rankings should be empty")
def verify_empty_rankings():
    assert rankings == []

