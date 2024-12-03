# Coding_Challenge
SPAN Coding challenge

# League Ranking Table Calculator

## Problem Statement & Instructions

This project requires the development of a **production-ready**, **maintainable**, and **testable** command-line application to calculate the ranking table for a league. The solution should:

- Be written in **Java**, **Python**, **Golang**, or **Scala**.
- Include **supporting tests**.
- Be presented for a code review, with the ability to explain the solution.

---

## Problem Description

The application processes game results and computes a league ranking table. 

### Input/Output
- **Input**: Text-based, either via `stdin/stdout` or filenames provided as command-line arguments.
  - Each line contains the result of one game.
  - Example input:
    ```
    Lions 3, Snakes 3
    Tarantulas 1, FC Awesome 0
    Lions 1, FC Awesome 1
    Tarantulas 3, Snakes 1
    Lions 4, Grouches 0
    ```
- **Output**: Ordered league ranking table (from most to least points), formatted as:
  ```
   1. Tarantulas, 6 pts
   2. Lions, 5 pts
   3. FC Awesome, 1 pt
   3. Snakes, 1 pt
   5. Grouches, 0 pts
  ```

  ---

## Rules
1. A **win** is worth **3 points**, a **draw** (tie) is worth **1 point**, and a **loss** is worth **0 points**.
2. Teams with the **same number of points**:
 - Share the same rank.
 - Are listed in **alphabetical order** within their rank.

---

## Guidelines
- Use libraries installed via a common package manager (e.g., `pip`) if necessary, but do not commit the installed packages.
- Include **automated tests**.
- Document any **complicated setup steps**.

---

## Platform Support
- The solution will run in a **Unix-like environment** (e.g., OS X).
- Use **platform-agnostic constructs** where possible to avoid issues like:
- Line endings.
- File path separators.

---

## Development Notes
- Ensure the application is **testable** by writing automated tests.
- Consider edge cases such as:
  - No matches played.
  - Ties with varying scores.
- Handle **input validation** gracefully.


## General Notes
- This solution uses BDD as a main way to run automated test
- To run the pytest solution is necessary the libraries pytest-bdd and pytest installed throgh pip commands
- Enable discovery either by Visual Studio or maually through the settings file and select and select pytest as the framework


- It also comes with a simple solution that is located under the folder CHALLENGE -> Simple_test_ranking_matches
  - In order to run the simple test go to the directory and use command line like this :
  - python coding_test.py matches.txt
  - For any change in the values of the input make modifications to matches.txt
