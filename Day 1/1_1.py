file_path = "1_1input.txt"

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def isDigit(str):
    if str.toLower() in digits:
        return True
    return False

digitToInt = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

with open(file_path, 'r') as file:
    lines = file.readlines()
    sum = 0

    for line in lines:
        first = True
        ans = ""
        last = ""
        for i in range(len(line)):

            digit = ""

            if line[i].isdigit():
                if first:
                    first = False
                    ans += line[i]
                
                last = line[i]
            else:
                flag = False
                for j in range(i,i+3):
                    if j >= len(line):
                        flag = True
                        break
                    digit += line[j]
                
                if flag == False:
                    if digit in digits:
                        if first:
                            first = False
                            ans += digitToInt[digit]
                
                        last = digitToInt[digit]
                    else:
                        for j in range(i+3,i+5):
                            if j >= len(line):
                                break
                            
                            digit += line[j]

                            if digit in digits:
                                if first:
                                    first = False
                                    ans += digitToInt[digit]
                        
                                last = digitToInt[digit]
                        


        ans += last

        if ans != "":
            sum += int(ans)

print(sum)

            
