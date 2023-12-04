day = 2
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


max1 = {
    "red": 12,
    "green": 13,
    "blue": 14
}

max = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for path in [test_path, file_path]:

    with open(path, 'r') as file:
        ans = 0
        sum1 = 0
        sum2 = 0
        lines = file.readlines()

        for line in lines:
            max["red"] = 0
            max["green"] = 0
            max["blue"] = 0


            game_info, rolls_info = line.split(':')
            game_id = int(game_info.split()[1])
            sum1 += game_id
            
            rolls = rolls_info.strip().split(';')


            flag = False

            for roll in rolls:

                for item in roll.split(','):
                    count, colour = item.strip().split()
                    if int(count) > max[colour]:
                        max[colour] = int(count)
                        
                    
                    if not flag and int(count) > max1[colour]:
                        flag = True
                        ans += game_id
                
            
            sum2 += max["red"] * max["green"] * max["blue"]



    print("="*80)
    print(sum1-ans, sum2)
