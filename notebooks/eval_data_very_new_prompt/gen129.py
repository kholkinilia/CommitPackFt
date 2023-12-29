from typing import List

# the bug in minPath is that the path is not calculated correctly
# the path is calculated by going through all the cells in the grid
# but the grid is not updated after each cell is visited
# to fix it we need to update the grid after each cell is visited
# here is the correct implementation

def minPath(grid, k):
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp = []
                if i!= 0:
                    temp.append(grid[i][j])

                if j!= 0:
                    temp.append(grid[i][j])

                if i!= n - 1:
                    temp.append(grid[i][j])

                if j!= n - 1:
                    temp.append(grid[i][j])

                val = min(temp)

    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans