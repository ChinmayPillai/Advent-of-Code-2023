import sys
day = 23
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


def valid(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False


direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

possible_dir = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

for path in [test_path, file_path]:

    ans = 0
    with open(path, 'r') as file:
        grid = [line.strip() for line in file.read().split('\n')]

    st_i, st_j = 0, 1
    rows, cols = len(grid), len(grid[0])
    recst = [[False] * cols for _ in range(rows)]

    dp = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                dp[i][j] = float('inf')

    dp[st_i][st_j] = 0

    q = [(st_i, st_j, 0, 0)]
    steps = 0

    while q:
        steps += 1
        nodes = len(q)

        for i in range(nodes):
            x, y, di, dj = q.pop(0)

            if x == rows-1:
                ans = max(ans, steps)
                continue

            for dx, dy in direc:

                nx = x + dx
                ny = y + dy

                if not valid(grid, nx, ny) or grid[nx][ny] == '#' or (dx, dy) == (-di, -dj):
                    continue

                if grid[x][y] in "^v<>" and ((dx, dy) != possible_dir[grid[x][y]] or grid[nx][ny] != '.'):
                    continue

                q.append((nx, ny, dx, dy))

    print("="*80)
    print(ans-1)

    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    points = [start, end]

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for dx, dy in direc:
                nx = r + dx
                ny = c + dy

                if valid(grid, nx, ny) and grid[nx][ny] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))

    graph = {pt: {} for pt in points}

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()
            
            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dx, dy in direc:
                nx = r + dx
                ny = c + dy
                if valid(grid, nx, ny) and grid[nx][ny] != "#" and (nx, ny) not in seen:
                    stack.append((n + 1, nx, ny))
                    seen.add((nx, ny))

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    print(dfs(start))
    print("="*80)
