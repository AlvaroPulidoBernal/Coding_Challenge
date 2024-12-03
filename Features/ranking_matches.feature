Feature: Calculate team rankings
  As a user
  I want to calculate team rankings based on match results
  So that I can see the rankings sorted by points and tiebreakers

  Scenario: Calculate rankings from a set of matches
    Given the following matches:
      | match                  |
      | Lions 3, Snakes 3      |
      | Tarantulas 1, FC Awesome 0 |
      | Lions 1, FC Awesome 1  |
      | Tarantulas 3, Snakes 1 |
      | Lions 4, Grouches 0    |
    When I calculate the rankings
    Then the rankings should be:
      | ranking                     |
      | 1. Tarantulas, 6 pts        |
      | 2. Lions, 5 pts             |
      | 3. FC Awesome, 1 pt         |
      | 3. Snakes, 1 pt             |
      | 5. Grouches, 0 pts          |


  Scenario: Handle an empty list of matches
    Given no matches
    When I calculate the rankings
    Then the rankings should be empty

  Scenario: Handle matches with tied rankings
    Given the following matches:
      | match                  |
      | Lions 1, Snakes 1      |
      | Tarantulas 0, FC Awesome 0 |
      | Grouches 2, Lions 2    |
    When I calculate the rankings
    Then the rankings should be:
      | ranking                |
      | 1. Lions, 2 pts        |
      | 2. FC Awesome, 1 pt    |
      | 2. Grouches, 1 pt      |
      | 2. Snakes, 1 pt        |
      | 2. Tarantulas, 1 pt    |

  Scenario: Handle a single match
    Given the following matches:
      | match                  |
      | Lions 3, FC Awesome 0  |
    When I calculate the rankings
    Then the rankings should be:
      | ranking                     |
      | 1. Lions, 3 pts             |
      | 2. FC Awesome, 0 pts        |