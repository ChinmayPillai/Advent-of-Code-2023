day = 22
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

from collections import deque

def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for path in [test_path, file_path]:

    ans = 0
    with open(path, 'r') as file:
        lines = [line.strip() for line in file.read().split('\n')]

    bricks = []
    for line in lines:
        coordinates = list(map(int, line.replace("~", ",").split(',')))
        bricks.append(coordinates)

    bricks.sort(key=lambda brick: brick[2])


    for index, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z
        
    bricks.sort(key=lambda brick: brick[2])

    k_supports_v = {i: set() for i in range(len(bricks))}
    v_supportedBy_K = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supportedBy_K[j].add(i)
    
    total = 0

    for i in range(len(bricks)):
        if all(len(v_supportedBy_K[j]) >= 2 for j in k_supports_v[i]):
            total += 1

    print(total)

    total = 0

    for i in range(len(bricks)):
        q = deque(j for j in k_supports_v[i] if len(v_supportedBy_K[j]) == 1)
        falling = set(q)
        falling.add(i)
        
        while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling:
                if v_supportedBy_K[k] <= falling:
                    q.append(k)
                    falling.add(k)
        
        total += len(falling) - 1

    print(total)
    print("="*80)
