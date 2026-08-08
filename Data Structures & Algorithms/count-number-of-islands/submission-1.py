class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0]) 
        
        def dfs(r, c):
            stack = [(r, c)]
            
            while stack:
                row, col = stack.pop()
                
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                if grid[row][col] == '0':
                    continue
                
                grid[row][col] = '0'
                stack.append((row-1, col))
                stack.append((row+1, col))
                stack.append((row, col-1))
                stack.append((row, col+1))
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        
        return count
