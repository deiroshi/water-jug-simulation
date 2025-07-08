from collections import deque

class FourGallonWaterSolver:
    def __init__(self, bucket1_capacity, bucket2_capacity, target):
        self.bucket1_capacity = bucket1_capacity # 3-gallon bucket
        self.bucket2_capacity = bucket2_capacity # 5-gallon bucket
        self.target = target
        self.initial_state = (0, 0)

    def possible_moves(self, state): # All possible actions from a given state
        bucket1, bucket2 = state
        moves = []

        # Fill bucket 1 (3-gallon)
        if bucket1 < self.bucket1_capacity:
            moves.append((self.bucket1_capacity, bucket2, f"Fill 3-gallon bucket"))

        # Fill bucket 2 (5-gallon)
        if bucket2 < self.bucket2_capacity:
            moves.append((bucket1, self.bucket2_capacity, f"Fill 5-gallon bucket"))       

        # Empty bucket 1 (3-gallon)
        if bucket1 > 0:
            moves.append((0, bucket2, f"Empty 3-gallon bucket"))

        # Empty bucket 2 (5-gallon)
        if bucket2 > 0:
            moves.append((bucket1, 0, f"Empty 5-gallon bucket"))
        
        # Pour from bucket 1 to bucket 2 (3-gallon to 5-gallon)
        if bucket1 > 0 and bucket2 < self.bucket2_capacity:
            pour_amount = min(bucket1, self.bucket2_capacity - bucket2)
            moves.append((bucket1 - pour_amount, bucket2 + pour_amount, f"Pour from 3-gallon to 5-gallon"))

        # Pour from bucket 2 to bucket 1 (5-gallon to 3-gallon)
        if bucket2 > 0 and bucket1 < self.bucket1_capacity:
            pour_amount = min(bucket2, self.bucket1_capacity - bucket1)
            moves.append((bucket1 + pour_amount, bucket2 - pour_amount, f"Pour from 5-gallon to 3-gallon"))
            
        return moves
    
    def solve(self): #BFS
        visited = set()
        queue = deque([(self.initial_state, [])])  # State, path of actions

        while queue:
            current_state, path = queue.popleft()
            bucket1, bucket2 = current_state

            # Check if target is reached
            if (bucket1, bucket2) == (0, self.target):
                for step in path:
                    print(step)
                print(f"Goal reached with state: {current_state}")
                return path

            # Skip already visited states
            if current_state in visited:
                continue

            visited.add(current_state)

            # Explore all next possible moves
            for next_state, action in [(move[:2], move[2]) for move in self.possible_moves(current_state)]:
                if next_state not in visited:
                    queue.append((next_state, path + [action]))

        print("No solution found.")
        return None

if __name__ == "__main__": 
    solver = FourGallonWaterSolver(3, 5, 4)
    solver.solve()