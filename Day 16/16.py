day = 16
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

from collections import deque

def valid(i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False

def calc(r, c, dr, dc):
    # r, c, dr, dc
    a = [(r, c, dr, dc)]
    seen = set()
    q = deque(a)

    while q:
        r, c, dr, dc = q.popleft()

        r += dr
        c += dc

        if not valid(r,c):
            continue

        ch = grid[r][c]
        
        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
                    
    coords = {(r, c) for (r, c, _, _) in seen}
    
    return len(coords)


for path in [test_path, file_path]:
    print("="*80)

    with open(path, 'r') as file:
        grid = open(path, 'r').read().split('\n')

    ans1 = calc(0, -1, 0, 1);
    print(ans1)

    max_val = ans1
    
    for r in range(len(grid)):
        max_val = max(max_val, calc(r, -1, 0, 1))
        max_val = max(max_val, calc(r, len(grid[0]), 0, -1))
        
    for c in range(len(grid)):
        max_val = max(max_val, calc(-1, c, 1, 0))
        max_val = max(max_val, calc(len(grid), c, -1, 0))

    print(max_val)
    print("="*80)


          

    

    