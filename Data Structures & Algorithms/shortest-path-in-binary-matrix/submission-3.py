class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        n=len(grid)
        if grid[0][0] ==1 or grid[n-1][n-1]== 1:
            return -1
        queue =deque([(0,0)])
        grid[0][0] = 1
        count=1
        directions = [
                (-1, 0),   # up
                (1, 0),    # down
                (0, -1),   # left
                (0, 1),    # right
                (-1, -1),  # up-left
                (-1, 1),   # up-right
                (1, -1),   # down-left
                (1, 1)     # down-right
                ]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r,c=queue.popleft()
                if r == n - 1 and c == n - 1:
                    return count
           
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    
                    if 0<= nr < n and 0<= nc < n:
                        if grid[nr][nc] == 0:
                            
                            grid[nr][nc]=1
                            queue.append((nr,nc))
            count+=1 
        return -1  

