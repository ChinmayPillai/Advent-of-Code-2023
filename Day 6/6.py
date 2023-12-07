day = 6
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


for path in [test_path, file_path]:
    

    ans = 1
    ans2 = 0

    with open(path, 'r') as file:
        lines = file.readlines()
        time_list = []
        distance_list = []
        time_combined = 0
        distance_combined = 0

        for i, line in enumerate(lines):
            # Split each line into words
            words = line.split()
            
            # Check if the line contains time or distance
            if words[0] == 'Time:':
                # Extract time values and convert them to integers
                time_list = [int(time) for time in words[1:]]
                time_combined = int(''.join(words[1:]))
            elif words[0] == 'Distance:':
                # Extract distance values and convert them to integers
                distance_list = [int(distance) for distance in words[1:]]
                distance_combined = int(''.join(words[1:]))

        # Combine time and distance lists into pairs
        pairs = list(zip(time_list, distance_list))
        
        for t, d in pairs:
            sum = 0
            for x in range(1, t):
                if x*t - x*x > d:
                    #print("x: ", x)
                    #print(x*(1+t) - x*x)
                    sum += 1
            if sum > 0:
                ans *= sum
                #print(sum, "\n")
        
        for x in range(1,time_combined):
            if x*time_combined - x*x > distance_combined:
                ans2 += 1

    
    print("="*80)
    print(ans, ans2)
    print("="*80)