day = 2
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"
ans = 0

sum = 0

max = {
    "red": 0,
    "green": 0,
    "blue": 0
}

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        max["red"] = 0
        max["green"] = 0
        max["blue"] = 0


        game_info, rolls_info = line.split(':')
        game_id = int(game_info.split()[1])
        #sum += game_id
        
        rolls = rolls_info.strip().split(';')


        for roll in rolls:

            flag = False
            for item in roll.split(','):
                count, colour = item.strip().split()
                if int(count) > max[colour]:
                    max[colour] = int(count)
                    #flag = True
                    #ans += game_id
                    #break
            
            #if flag:
            #    break
        
        sum += max["red"] * max["green"] * max["blue"]




print(sum)

#print(sum-ans)