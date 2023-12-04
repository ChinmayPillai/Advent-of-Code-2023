day = 3
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"




for path in [test_path, file_path]:

    with open(path, 'r') as file:
        rows = file.readlines()
        ans = 0
        num = 0

        # Define directions for adjacent cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]

        # Function to check if a position is within bounds
        def is_valid(x, y):
            return 0 <= x < len(rows) and 0 <= y < len(rows[x])

        # Function to check if a number or any of its digits has non-period symbols adjacent to it
        def has_non_period_adjacent(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and rows[nx][ny] not in ['.', '\n'] and not rows[nx][ny].isdigit():
                    return True
            # print(x,y,rows[x][y])
            return False

        num = 0
        sym = False
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if rows[i][j].isdigit() == False:
                    if sym == True:
                        ans += num
                    num = 0
                    sym = False
                else:
                    num = num * 10 + int(rows[i][j])
                    if has_non_period_adjacent(i, j):
                        sym = True

        # for i in range(len(rows)):
        #     for j in range(len(rows[i])):
        #         if rows[i][j].isdigit() == False:
        #             continue

        #         if has_non_period_adjacent(i,j) == True:
        #             #print(i,j)
        #             num = int(rows[i][j])
        #             p = j
        #             k = 10
        #             while is_valid(i,p-1) and rows[i][p-1].isdigit():
        #                 print(num)
        #                 temp = num
        #                 num = int(rows[i][p-1]) * k + temp
        #                 k *= 10
        #                 p -= 1
        #             print(num)
        #             print("-"*10)
        #             p = j
        #             while is_valid(i,p+1) and rows[i][p+1].isdigit():
        #                 #print(num)
        #                 temp = num
        #                 num = temp * 10 + int(rows[i][p+1])
        #                 rows[i] = rows[i][:p + 1] + '.' + rows[i][p + 2:]
        #                 p += 1
        #             #print(num)
        #             #print("-"*20)
        #             ans += num

    print("="*80)
    print(ans)
