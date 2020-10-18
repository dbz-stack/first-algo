def max_killed_enemies(grid):
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    max_killed = 0
    row_e, col_e = 0, [0] * n
    # iterates over all cells in the grid
    for i in range(m):
        for j in range(n):
            # makes sure we are next to a wall.
            if j == 0 or grid[i][j-1] == 'W':
                row_e = row_kills(grid, i, j)
            # makes sure we are next to a wall.
            if i == 0 or grid[i-1][j] == 'W':
                col_e[j] = col_kills(grid, i, j)
            # makes sure the cell contains a 0
            if grid[i][j] == '0':
                # updates the variable
                max_killed = max(max_killed, row_e + col_e[j])

    return max_killed

# calculate killed enemies for row i from column j
def row_kills(grid, i, j):
    num = 0
    len_row = len(grid[0])
    while j < len_row and grid[i][j] != 'W':
        if grid[i][j] == 'E':
            num += 1
        j += 1
    return num

# calculate killed enemies for  column j from row i
def col_kills(grid, i, j):
    num = 0
    len_col = len(grid)
    while i < len_col and grid[i][j] != 'W':
        if grid[i][j] == 'E':
            num += 1
        i += 1
    return num
                


# ----------------- TESTS -------------------------

"""
    Testsuite for the project
"""

import unittest 

class TestBombEnemy(unittest.TestCase):
    def test_3x4(self):
        grid1 = [["0","E","0","0"],
                ["E","0","W","E"],
                ["0","E","0","0"]]
        self.assertEqual(3,max_killed_enemies(grid1))
    def test_4x4(self):
        grid1 = [
                ["0", "E", "0", "E"],
                ["E", "E", "E", "0"],
                ["E", "0", "W", "E"],
                ["0", "E", "0", "0"]]
        grid2 = [
                ["0", "0", "0", "E"],
                ["E", "0", "0", "0"],
                ["E", "0", "W", "E"],
                ["0", "E", "0", "0"]]
        self.assertEqual(5,max_killed_enemies(grid1))
        self.assertEqual(3,max_killed_enemies(grid2))

if __name__ == "__main__":
    unittest.main()
