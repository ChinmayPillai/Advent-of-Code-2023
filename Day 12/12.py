day = 12
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


def count_arrangements(row, damaged_groups):
    n = len(row)
    m = max(damaged_groups) + 1
    dp = [[0] * m for _ in range(n)]

    # Initialize the first position for the first damaged group
    dp[0][damaged_groups[0] - 1] = 1 if row[0] == '.' else 0
    print(dp[0])

    # Fill in the dp array
    for i in range(1, n):
        for j in range(m):
            if row[i] == '.':
                dp[i][j] = dp[i - 1][j - 1] if j > 0 else 0
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] if j > 0 else dp[i - 1][j]

    # Calculate the total arrangements for each damaged group size
    total_arrangements = sum(dp[n - 1][g - 1] for g in damaged_groups)

    return total_arrangements


for path in [test_path, file_path]:

    with open(path, 'r') as file:
        lines = [line.strip() for line in file.read().split('\n')]
        G = [[c for c in line] for line in lines]
    DP = {}
    def f(dots, blocks, i, bi, current):
        key = (i, bi, current)
        if key in DP:
            return DP[key]
        if i==len(dots):
            if bi==len(blocks) and current==0:
                return 1
            elif bi==len(blocks)-1 and blocks[bi]==current:
                return 1
            else:
                return 0
        ans = 0
        for c in ['.', '#']:
            if dots[i]==c or dots[i]=='?':
                if c=='.' and current==0:
                    ans += f(dots, blocks, i+1, bi, 0)
                elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
                    ans += f(dots, blocks, i+1, bi+1, 0)
                elif c=='#':
                    ans += f(dots, blocks, i+1, bi, current+1)
        DP[key] = ans
        return ans

    for part2 in [False,True]:
        ans = 0
        for line in lines:
            dots, blocks = line.split()
            if part2:
                dots = '?'.join([dots, dots, dots, dots, dots])
                blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
            blocks = [int(x) for x in blocks.split(',')]
            DP.clear()
            score = f(dots, blocks, 0, 0, 0)
            ans += score
        print(ans)

    print("="*80)

