day = 3
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


for path in [test_path, file_path]:

    with open(path, 'r') as file:
        rows = file.readlines()

        cs = set()
        ans1 = 0
        ans2 = 0

        for i, row in enumerate(rows):
            for j, ch in enumerate(row):
                if ch.isdigit() or ch in ['.', '\n']:
                    continue
                gearCnt = 0
                gearRat = 1
                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if x < 0 or x >= len(rows) or y < 0 or y >= len(rows[x]) or not rows[x][y].isdigit():
                            continue
                        while y > 0 and rows[x][y-1].isdigit():
                            y -= 1
                        
                        if (x, y) not in cs:
                            b = y
                            gearCnt += 1
                            s = ""
                            while y < len(rows[x]) and rows[x][y].isdigit():
                                s += rows[x][y]
                                y += 1
                            ans1 += int(s)
                            gearRat *= int(s)
                            cs.add((x,b))
                
                if gearCnt == 2:
                    ans2 += gearRat

        print(ans1, ans2)
        

        


        

   
