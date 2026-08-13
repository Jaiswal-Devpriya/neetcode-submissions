class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_l, col_l = len(grid),len(grid[0])
        queue = deque()
        fresh=0
        minutes=0
        for r in range(row_l):
            for c in range(col_l):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while queue and fresh>0:
            level_size=len(queue)
           
            for _ in range(level_size):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<row_l and 0<=nc <col_l:
                        if grid[nr][nc] == 2 or grid[nr][nc] ==0:
                            continue
                        elif grid[nr][nc]==1:
                            grid[nr][nc]=2
                            fresh=fresh-1
                            queue.append((nr,nc))
                            
                            
           
            minutes += 1                    
       
        return -1 if fresh > 0 else minutes
        


        