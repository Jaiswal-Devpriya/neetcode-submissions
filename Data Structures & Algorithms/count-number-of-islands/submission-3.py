class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0]) 
        queue=deque()
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        land =0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                if grid[r][c] == "1":
                    land += 1

                    grid[r][c] = "0"      
                    queue.append((r, c))

                    while queue:
                        r,c=queue.popleft()
                        
                        for dr,dc in directions:
                            nr = r+dr
                            nc=c+dc

                            if 0<=nr<rows and 0<=nc<cols:
                                if grid[nr][nc]=='1':
                                    grid[nr][nc]='0'
                                    queue.append((nr,nc))
        return land