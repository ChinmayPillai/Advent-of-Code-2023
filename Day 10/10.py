day = 10
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


direc = [(0,1), (1,0), (-1,0), (0,-1)]

allowed_paths = {
    '|' : [(1,0), (-1,0)],
    '-' : [((0,1)), (0, -1)],
    'L' : [(-1,0), (0, 1)],
    'J' : [(-1,0), (0, -1)],
    'F' : [(1,0), (0, 1)],
    '7' : [(1,0), (0, -1)],
    'S' : [(0,1), (1,0), (-1,0), (0,-1)],
    '.' : []
}

allowed_prev = {
    '|' : ['|','J','L','F','7'],
    '-' : ['-','J','L','F','7'],
    'L' : ['|','-','J','L','F','7'],
    'J' : ['|','-','J','L','F','7'],
    'F' : ['|','-','J','L','F','7'],
    '7' : ['|','-','J','L','F','7'],
    'S' : ['|','-','J','L','F','7'],
}

def isValid(grid, i,j):
    if 0<=i<len(grid) and 0<=j<len(grid[i]):
        return True
    return False

#DFS
def loopFn(grid, a, b):

    st = [(a,b)]

    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    loop = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    
    loop[a][b] = True

    s = {'|','-','J','L','F','7'}

    while len(st) > 0:
        x, y = st.pop()
        visited[x][y] = True

        for dx,dy in allowed_paths[grid[x][y]]:
            newX = x + dx
            newY = y + dy

            if isValid(grid, newX, newY) and not visited[newX][newY] and (-dx, -dy) in allowed_paths[grid[newX][newY]]:
                loop[newX][newY] = True
                st.append((newX,newY))

                #Find 'S
                if grid[x][y] == 'S':
                    if grid[newX][newY] == '|':
                        if (dx,dy) == (-1, 0):
                            s &= {'|','J','L'}
                        else:
                            s &= {'|', 'F','7'}
                    elif grid[newX][newY] == 'F':
                        if (dx,dy) == (-1, 0):
                            s &= {'|','J','L'}
                        else:
                            s &= {'-','J','7'}
                    elif grid[newX][newY] == 'L':
                        if (dx,dy) == (1, 0):
                            s &= {'|','F','7'}
                        else:
                            s &= {'-','J','7'}
                    elif grid[newX][newY] == '-':
                        if (dx,dy) == (0, 1):
                            s &= {'-', 'F','L'}
                        else:
                            s &= {'-','J','7'}
                    elif grid[newX][newY] == 'J':
                        if (dx,dy) == (0, 1):
                            s &= {'-', 'F','L'}
                        else:
                            s &= {'|', 'F','7'}
                    elif grid[newX][newY] == '7':
                        if (dx,dy) == (0, 1):
                            s &= {'-', 'F','L'}
                        else:
                            s &= {'|','J','L'}


    return s, loop

for path in [test_path, file_path]:

    with open(path, 'r') as file:
        lines = file.read().split('\n')
    grid = [list(line.strip()) for line in lines]

    flag = False
    #Find Start
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                
                (start_x, start_y) = (i,j)
                s, loop = loopFn(grid, i,j)
                assert len(s) == 1
                (start_ch,) = s
                #print(start_ch)
                break

        if(flag):
            break
    
    loops = set()
    
    grid[start_x][start_y] = start_ch
    #DFS
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if loop[i][j] == False:
                grid[i][j] = '.'
            else:
                loops.add((i,j))

    #BFS
    q = []
    q.append((start_x, start_y))
    dis = 0
    
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]

    while len(q)>0:
        dis += 1
        nodes = len(q)

        for k in range(nodes):
            x, y = q.pop(0)

            for dx, dy in allowed_paths[grid[x][y]]:
                newX = x + dx
                newY = y + dy
                if isValid(grid, newX, newY) and not visited[newX][newY] and (-dx,-dy) in allowed_paths[grid[newX][newY]]:
                    q.append((newX, newY))
                    visited[newX][newY] = True
    #print(q, dis)

    #Find area of inside points
    outside = set()
    for r, row in enumerate(grid):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"unexpected character (horizontal): {ch}")
            
            if not within:
                outside.add((r, c))
            
    ans = len(grid) * len(grid[0]) - len(outside | loops)

        

          
    print("="*80)
    print(dis-1, ans)
    print("="*80)