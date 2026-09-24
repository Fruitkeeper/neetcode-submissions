from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: 
            return -1  # Edge case: empty grid
        
        # Initialize the queue for BFS
        queue = deque()
        fresh_oranges = 0  # Count of fresh oranges
        
        # Step 1: Add all rotten oranges to the queue and count fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 2: 
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # If there are no fresh oranges, return 0 (nothing to rot)
        if fresh_oranges == 0:
            return 0
        
        # Step 2: BFS to spread the rot
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0  # Time counter
        
        while queue:
            for _ in range(len(queue)):  # Process all nodes in the current minute
                x, y = queue.popleft()
                for dx, dy in directions: 
                    nx, ny = x + dx, y + dy 
                    # If the neighboring cell is a fresh orange, rot it
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1: 
                        grid[nx][ny] = 2  # Mark as rotten
                        queue.append((nx, ny))  # Add to queue
                        fresh_oranges -= 1  # Reduce fresh orange count
            
            # Only increment time if there are still oranges rotting
            if queue:
                minutes += 1
        
        # Step 3: Check if all fresh oranges are rotted
        return minutes if fresh_oranges == 0 else -1

        