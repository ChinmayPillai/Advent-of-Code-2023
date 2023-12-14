day = 14
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

def load(platform):
    total_load = 0
    rows, cols = len(platform), len(platform[0])
    #print(rows, cols)

    for row in range(rows):
        for col in range(cols):
            if platform[row][col] == 'O':
                total_load += rows - row

    return total_load

def tilt_platform(platform, direction):
    rows, cols = len(platform), len(platform[0])
    if direction == 'north':
        #print("Tilt platform")
        for col in range(cols):
            for row in range(rows):
                if platform[row][col] == 'O':
                    row = row - 1
                    while 0 <= row < rows and platform[row][col] == '.':
                        #print("Roll")
                        platform[row][col] = 'O'
                        platform[row+1][col] = '.'
                        row -= 1

        return platform
    elif direction == 'south':
        for col in range(cols):
            for row in range(rows-1, -1, -1):
                if platform[row][col] == 'O':
                    row = row + 1
                    while 0 <= row < rows and platform[row][col] == '.':
                        #print("Roll")
                        platform[row][col] = 'O'
                        platform[row-1][col] = '.'
                        row += 1
        return platform
    elif direction == 'east':
        for row in range(rows):
            for col in range(cols-1, -1, -1):
                if platform[row][col] == 'O':
                    col = col + 1
                    while 0 <= col < cols and platform[row][col] == '.':
                        #print("Roll")
                        platform[row][col] = 'O'
                        platform[row][col-1] = '.'
                        col += 1
        return platform
    elif direction == 'west':
        for row in range(rows):
            for col in range(cols):
                if platform[row][col] == 'O':
                    col = col - 1
                    while 0 <= col < cols and platform[row][col] == '.':
                        #print("Roll")
                        platform[row][col] = 'O'
                        platform[row][col+1] = '.'
                        col -= 1

        return platform
    
for path in [test_path, file_path]:
    print("="*80)

    with open(path, 'r') as file:
        tilted_platform = [list(line.strip()) for line in file.read().split('\n')]
    
    #print(lines)

    grid = {}
    cycles = 1000000000
    i = 0

    while i < cycles:
        i += 1
        
        tilted_platform = tilt_platform(tilted_platform, 'north')
        if i == 1:
            print(load(tilted_platform))
        tilted_platform = tilt_platform(tilted_platform, 'west')
        tilted_platform = tilt_platform(tilted_platform, 'south')
        tilted_platform = tilt_platform(tilted_platform, 'east')

        res = tuple(tuple(row) for row in tilted_platform)

        if res in grid:
            cycle_length = i-grid[res]
            amt = (cycles-i)//cycle_length
            i += amt * cycle_length
        grid[res] = i

    #print(tilted_platform)

    # Calculate the total load on the north support beams
    total_load = load(tilted_platform)

    
    print(total_load)
    print("="*80)