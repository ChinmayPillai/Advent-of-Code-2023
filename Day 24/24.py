day = 24
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

import sympy

for path in [file_path]:
    
    ans = 0
    with open(path, 'r') as file:
        lines = [line.strip() for line in file.read().split('\n')]

    hailstones = []

    dic = {}

    for line in lines:
        p, v = line.split(' @ ')
        px,py,pz = map(int, p.split(', '))
        vx,vy,vz = map(int, v.split(', '))
        hailstones.append((px,py,pz,vx,vy,vz))
    
    # Adjust the test area boundaries as needed
    x_min, x_max = 200000000000000, 400000000000000
    y_min, y_max = 200000000000000, 400000000000000

    for i, hs1 in enumerate(hailstones):
        #Parametric to Standard Form
        p1, p2, p3, v1, v2, v3 = hs1
        a2, b2, c2 = v2, -v1, v2 * p1 - v1 * p2
        
        for hs2 in hailstones[:i]:            
            #Parametric to Standard Form
            p1, p2, p3, v1, v2, v3 = hs2
            a1, b1, c1 = v2, -v1, v2 * p1 - v1 * p2

            if a1 * b2 == b1 * a2:
                continue

            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if x_min <= x <= x_max and y_min <= y <= y_max:
                if all((x - hs[0]) * hs[3] >= 0 and (y - hs[1]) * hs[4] >= 0 for hs in (hs1, hs2)):
                    ans += 1
    
    print("="*80)
    print(ans)


    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

    equations = []

    for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
        #px, py, pyz, vx, vy, vz of solution needs to collide with hailstone at same time 't'
        #=> t1 = t2
        #For all hailstones
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]

        #If only 1 interger answer left, only that can be the answer (given answer existst)
        #Hence better to compute everytime and exit quickly than make one big computation at the end
        if len(answers) == 1:
            break
        
    answer = answers[0]

    print(answer[xr] + answer[yr] + answer[zr])

    print("="*80)