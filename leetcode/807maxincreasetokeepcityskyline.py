class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        v1,v2 = [],[]
        for i in grid:
            v1.append(max(i))
        for j in range(len(grid[0])):
            t=[]
            for i in range(len(grid)):
                t.append(grid[i][j])
            v2.append(max(t))

        # top_max.append(max(item[i] for item in grid))
        s = 0
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                t=min(v1[i],v2[j])
                if grid[i][j] < t:
                    t -= grid[i][j]
                    s += t
        return s


        #from discuss
        # grid_t = zip(*grid)
        #
        # # Vertical and horizontal skylines
        # sk_v = [max(row) for row in grid]  # As seen from left/right
        # sk_h = [max(row) for row in grid_t]  # As seen from top/bottom