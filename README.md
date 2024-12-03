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
- 1. Tarantulas, 6 pts
- 2. Lions, 5 pts
- 3. FC Awesome, 1 pt
- 3. Snakes, 1 pt
- 5. Grouches, 0 pts
