day = 21
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


def valid(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False


direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def count_paths(grid, steps):
    rows, cols = len(grid), len(grid[0])
    dp = [[[0] * cols for _ in range(rows)] for _ in range(steps + 1)]

    # Initialize the starting position
    dp[0][st_i][st_j] = 1

    q = [(st_i, st_j)]

    # Dynamic programming to count paths
    for k in range(1, steps + 1):
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '#':
                    continue

                for dx, dy in direc:
                    ni, nj = (i + dx) % rows, (j + dy) % cols

                    if not valid(grid, ni, nj):
                        continue

                    if grid[ni][nj] != '#':
                        dp[k][i][j] += dp[k - 1][ni][nj]

    ans = 0
    # Sum up the paths at the destination plots after the specified number of steps
    for i in range(rows):
        for j in range(cols):
            if dp[steps][i][j] != 0:
                ans += 1

    return ans

def findD(r,c):
  D = {}
  Q = [(0,0,st_i,st_j,0)]
  while Q:
    tr,tc,r,c,d = Q.pop(0)
    if r<0:
      tr -= 1
      r += rows
    if r>=rows:
      tr += 1
      r -= rows
    if c<0:
      tc -= 1
      c += cols
    if c>=cols:
      tc += 1
      c -= cols
    assert valid(grid, r,c)

    if grid[r][c] =='#' or (tr,tc,r,c) in D:
      continue
    if abs(tr)>2 or abs(tc)>2:
      continue
    D[(tr,tc,r,c)] = d
    for dr,dc in direc:
      Q.append((tr,tc,r+dr, c+dc, d+1))
  return D

def solve(d,v,L):
  amt = (L-d)//rows
  if (d,v,L) in SOLVE:
    return SOLVE[(d,v,L)]
  ret = 0
  for x in range(1,amt+1):
    if d+rows*x<=L and (d+rows*x)%2==(L%2):
      ret += ((x+1) if v==2 else 1)
  SOLVE[(d,v,L)] = ret
  
  return ret

for path in [file_path]:

    ans = 0
    with open(path, 'r') as file:
        grid = [list(line.strip()) for line in file.read().split('\n')]
    

    rows = len(grid)
    cols = len(grid[0])

    st_i = -1
    st_j = -1


    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                st_i = i
                st_j = j
                break
        else:
            continue
        break

    assert st_i != -1
    assert st_j != -1

    result = count_paths(grid, 64)
    print(result)

    print("="*80)

    #Dictionary of all brute-force reachable points in finite repeated grid and min steps to reach them
    D = findD(st_i,st_j)
    SOLVE = {}

    def solve21(part1):
        L = (64 if part1 else 26501365)
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if (0,0,r,c) in D:
                
                    assert rows==cols
                    OPT = [-1,0,1]
                    for tr in OPT:
                        for tc in OPT:
                            if part1 and (tr!=0 or tc!=0):
                                continue
                            d = D[(tr,tc,r,c)]
                            if d%2==L%2 and d<=L:
                                ans += 1
                            if tr in [min(OPT),max(OPT)] and tc in [min(OPT),max(OPT)]:
                                ans += solve(d,2,L)
                            elif tr in [min(OPT),max(OPT)] or tc in [min(OPT),max(OPT)]:
                                ans += solve(d,1,L)
        return ans

    
    print(solve21(False))

    print("="*80)
