day = 9
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

def predict_value(sequence, part2):
    differences = []
    differences.append([int(sequence[i + 1]) - int(sequence[i]) for i in range(len(sequence) - 1)])

    while len(set(differences[-1])) > 1:
        differences.append([differences[-1][i + 1] - differences[-1][i] for i in range(len(differences[-1]) - 1)])

    for i in range(len(differences)-1, 0 , -1):
        differences[i-1].append(differences[i-1][-1] + differences[i][-1])
        differences[i-1].insert(0, differences[i-1][0] - differences[i][0])

    if not part2:
        return int(sequence[-1]) + differences[0][-1]
    return int(sequence[0]) - differences[0][0]

for path in [test_path, file_path]:
    
    ans = 0

    with open(path, 'r') as file:
        lines = file.readlines()
        next_value = []
        prev_value = []
        for i, line in enumerate(lines):
            seq = line.split()
            next_value.append(predict_value(seq, False))
            prev_value.append(predict_value(seq, True))


    
    print("="*80)
    print(sum(next_value), sum(prev_value))
    print("="*80)