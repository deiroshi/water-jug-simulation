# Water Jug Solver

A Python script that uses two water buckets (3-gallon and 5-gallon) to find a way to measure exactly 4 gallons of water.
It uses a Breadth-First Search (BFS) algorithm to try every possible action (fill, pour, empty) and stops when the goal is reached (in this case 0,4). 


## What it does

- Starts with two empty buckets: 3-gallon and 5-gallon  
- Tries all valid actions (filling, emptying, pouring)  
- Searches until the 5-gallon bucket has exactly 4 gallons  
- Prints out each step of the solution  


## Notes

- Only built-in Python libraries used (`collections.deque`)  
- Goal is to reach exactly 4 gallons in the 5-gallon bucket (in this case) 
- You can change the target amount in the code (e.g. `(3, 5, 2)`)  
- You can reuse the logic for other bucket sizes (e.g. 7 and 11 gallons)
