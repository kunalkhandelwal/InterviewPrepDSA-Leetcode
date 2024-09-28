#https://leetcode.com/problems/island-perimeter/description/

#Sol 0: Beats - 99% , 96%
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        
        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    ans+= 4

                    if r>0 and grid[r-1][c] == 1:
                        ans-=2
                    
                    if c>0 and grid[r][c-1] == 1:
                        ans-=2

        return ans
