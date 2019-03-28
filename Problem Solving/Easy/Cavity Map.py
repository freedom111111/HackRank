def cavityMap(grid):
    rows = len(grid)
    cols = len(grid[0])
    res = [grid[0]]
    if rows ==1 or cols==1:
        return grid
    else:
        for i in range(1,rows-1):
            ss = list(grid[i])
            for j in range(1,cols-1):
                if grid[i][j]> grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1]:
                    ss[j] = 'X'
            res.append(''.join(ss)) 
        res.append(grid[-1])
        return res
