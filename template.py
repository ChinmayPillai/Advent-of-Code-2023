day = 2
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


ans = 0

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        for ch in line:
            ans = 0


print(ans)