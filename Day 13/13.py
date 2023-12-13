day = 13
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


for path in [test_path, file_path]:
    
    ans = 0

    with open(path, 'r') as file:
        tests = open(path).read().strip().split('\n\n')
    
    tests = [ [ row for row in test.split('\n')]  for test in tests]

    for part2 in [False, True]:
        ans = 0
        for grid in tests:
            rows = len(grid)
            cols = len(grid[0])

            for c in range(cols-1):
                badness = 0
                for dc in range(cols):
                    left = c-dc
                    right = c+1+dc
                    if 0<=left<right<cols:
                        for r in range(rows):
                            if grid[r][left] != grid[r][right]:
                                badness += 1
                if badness == (1 if part2 else 0):
                    ans += c+1

            for r in range(rows-1):
                badness = 0
                for dr in range(rows):
                    up = r-dr
                    down = r+1+dr
                    if 0<=up<down<rows:
                        for c in range(cols):
                            if grid[up][c] != grid[down][c]:
                                badness += 1
                if badness == (1 if part2 else 0):
                    ans += 100*(r+1)
        print(ans)
    
    print("="*80)