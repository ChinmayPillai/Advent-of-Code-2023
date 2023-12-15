day = 15
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


def hash(s):
    value = 0
    for char in s:
        value = ( (value + ord(char)) * 17) % 256
    return value

def hashmap(Box, line):
    if line[-1] == '-':
        box = hash(line[:-1])
        reqBox = None

        for i, lens in enumerate(Box[box]):
            if lens[0] == line[:-1]:
                reqBox = i
                break
        
        if(reqBox != None):
            Box[box].pop(reqBox)
        

    else:
        box = hash(line[:-2])
        focal_length = int(line[-1])
        reqBox = None

        for i, lens in enumerate(Box[box]):
            if lens[0] == line[:-2]:
                reqBox = i
                break
        
        if(reqBox != None):
            Box[box][reqBox][1] = focal_length
        else:
            Box[box].append([line[:-2], focal_length])
        
    
    return


for path in [test_path, file_path]:
    
    ans1 = 0
    Box = [[] for i in range(256)]

    with open(path, 'r') as file:
        lines = file.read().strip().split(',')

    for line in lines:
        ans1 += hash(line)
        hashmap(Box, line)

    ans2 = 0
    
    for i in range(len(Box)):
        for j in range(len(Box[i])):
            ans2 += (i+1) * (j+1) * Box[i][j][1]

    
    print("="*80)
    print(ans1, ans2)
    print("="*80)