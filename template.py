file_path = "2.txt"
test_path = "test.txt"
ans = 0


with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        for ch in line:
            ans = 0


print(ans)