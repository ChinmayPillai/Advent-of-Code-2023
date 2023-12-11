day = 11
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


def isValid(i, j):
    if 0 <= i < len(lines) and 0 <= j < len(lines[0]):
        return True

    return False


direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for path in [test_path, file_path]:

    ans = 0

    with open(path, 'r') as file:
        lines = [list(line.strip()) for line in file.read().split('\n')]

    empty_rows = []
    empty_columns = []
    galaxies = []

    for i, line in enumerate(lines):
        flag = False
        for j, k in enumerate(line):
            if k == '#':
                flag = True

        if not flag:
            empty_rows.append(i)


    for j in range(len(lines[0])):
        flag = False
        for i in range(len(lines)):
            if lines[i][j] == '#':
                flag = True

        if not flag:
            empty_columns.append(j)


    for i, line in enumerate(lines):
        for j, k in enumerate(line):
            if k == '#':
                galaxies.append((i, j))


    for part2 in [False, True]:
        ans = 0
        for x, y in galaxies:
            for i, j in galaxies:
                ans += abs(x-i) + abs(y-j)
                for p in empty_rows:
                    if min(x, i) < p < max(x, i):
                        ans += 1000000-1 if part2 else 1
                for q in empty_columns:
                    if min(y, j) < q < max(y, j):
                        ans += 1000000-1 if part2 else 1

        print(ans//2)
    print("="*80)
