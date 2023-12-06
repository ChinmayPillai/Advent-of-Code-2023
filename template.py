day = 3
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


for path in [test_path, file_path]:
    
    ans = 0
    sum = 0

    with open(path, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            pass

    
    print("="*80)
    print(ans)
    print("="*80)