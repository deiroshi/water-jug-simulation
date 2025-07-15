# 4 Gallon Solver with Breadth-First Search

This project uses a **Breadth-First Search (BFS)** algorithm to solve the classic water jug problem.  
Given a 3-gallon and a 5-gallon bucket, the goal is to find the shortest sequence of steps to measure out **exactly 4 gallons** of water.


## Features

- Begins with two empty buckets: 3-gallon and 5-gallon
- Simulates all valid operations: fill, empty, pour between buckets
- Searches until the target state is reached (e.g. 0 gallons in the 3-gallon, 4 gallons in the 5-gallon bucket)
- Prints the complete step-by-step solution path


## Output Example

Fill 5-gallon bucket

Pour from 5-gallon to 3-gallon

Empty 3-gallon bucket

Pour from 5-gallon to 3-gallon

Fill 5-gallon bucket

Pour from 5-gallon to 3-gallon

Empty 3-gallon bucket

Goal reached with state: (0, 4)


## How It Works

1. **Initialization**  
   Begins with two empty buckets: `(0, 0)`

2. **Search Space**  
   Explores all valid transitions by applying fill, pour, and empty operations.

3. **BFS Algorithm**  
   Uses a queue to explore the shortest path to the target amount (e.g. `(0, 4)`)

4. **Goal Check**  
   Stops as soon as the 5-gallon bucket contains exactly 4 gallons


## Notes

- Goal and bucket sizes can be customized in the code (e.g. `(3, 5, 2)` or `(7, 11, 6)`)
- Reusable logic for solving similar "jug" or resource constraint problems
