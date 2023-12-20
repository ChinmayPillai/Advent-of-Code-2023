day = 20
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

def valid(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False




for path in [test_path, file_path]:
    
    ans = 0
    with open(path, 'r') as file:
        lines = [line.strip() for line in file.read().split('\n')]

    

    
    print("="*80)
    print(ans)
    print("="*80)