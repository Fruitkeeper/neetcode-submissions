class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        n, m = len(grid), len(grid[0])
        queue = deque()

        for i in range(n):
            for j in range(m): 
                if grid[i][j] == 0: 
                    queue.append((i,j))
        directions = ((1,0) , (0,1), (0,-1), (-1,0))
        while queue: 
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<= nx < n and 0<= ny < m and grid[nx][ny] == 2147483647: 
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx,ny))
