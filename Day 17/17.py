day = 17
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

from heapq import heappush, heappop

def valid(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False


for path in [test_path, file_path]:

    with open(path, 'r') as file:
        lines = [list(line.strip()) for line in file.read().split('\n')]

    grid = [[int(ch) for ch in line] for line in lines]

    for max_cons, min_cons in [(3,0), (10,4)]:
        seen = set()
        pq = [(0, 0, 0, 0, 0, 0)]

        while pq:
            heatLoss, x, y, dx, dy, n = heappop(pq)
            
            if x == len(grid) - 1 and y == len(grid[0]) - 1 and n >= min_cons:
                print(heatLoss)
                break

            if (x, y, dx, dy, n) in seen:
                continue

            seen.add((x, y, dx, dy, n))
            
            if n < max_cons and (dx, dy) != (0, 0):
                nx = x + dx
                ny = y + dy
                if valid(grid, nx, ny):
                    heappush(pq, (heatLoss + grid[nx][ny], nx, ny, dx, dy, n + 1))

            if n >= min_cons or (dx, dy) == (0, 0):
                for ndx, ndy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (ndx, ndy) != (dx, dy) and (ndx, ndy) != (-dx, -dy):
                        nx = x + ndx
                        ny = y + ndy
                        if valid(grid, nx, ny):
                            heappush(pq, (heatLoss + grid[nx][ny], nx, ny, ndx, ndy, 1))

    print("="*80)
