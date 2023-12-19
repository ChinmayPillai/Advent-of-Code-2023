day = 19
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


def part1(work, ratings):
    ans = 0

    for rating in ratings:
        next_name = "in"
        x = rating["x"]
        m = rating["m"]
        a = rating["a"]
        s = rating["s"]
        while True:
            if next_name == "A":
                ans += x
                ans += m
                ans += a
                ans += s
                break
            elif next_name == "R":
                break
            req = work[next_name]

            for eqn in req:
                if ":" in eqn:
                    condition, name = eqn.split(':')
                    if "<" in condition:
                        cat, num = condition.split("<")
                    elif ">" in condition:
                        cat, num = condition.split(">")
                    else:
                        print(condition, name)
                        assert False

                    val = rating[cat]

                    if "<" in condition:
                        if val < int(num):
                            next_name = name
                            break
                    elif ">" in condition:
                        if val > int(num):
                            next_name = name
                            break
                else:
                    next_name = eqn
                    break
    
    return ans
            

def part2(work):
    q = [((1,1,1,1), (4000,4000,4000,4000), "in")]

    ans = 0
    
    accepted = set()
    dic1 = {
        "x": None,
        "m": None,
        "a": None,
        "s": None,
    }

    dic2 = {
        "x": None,
        "m": None,
        "a": None,
        "s": None,
    }

    while q:
        #print(len(q))
        start, end, next_name = q.pop(0)
        dic1["x"], dic1["m"], dic1["a"], dic1["s"] = start
        dic2["x"], dic2["m"], dic2["a"], dic2["s"] = end
        #print(start, end, next_name)
        
        if next_name == "A":
            accepted.add( ((dic1["x"], dic1["m"], dic1["a"], dic1["s"]), (dic2["x"], dic2["m"], dic2["a"], dic2["s"])) )
            continue
        elif next_name == "R":
            continue
        req = work[next_name]

        for eqn in req:
            if ":" in eqn:
                condition, name = eqn.split(':')
                if "<" in condition:
                    cat, num = condition.split("<")
                elif ">" in condition:
                    cat, num = condition.split(">")
                else:
                    print(condition, name)
                    assert False

                num = int(num)

                if "<" in condition:
                    if dic2[cat] < num:
                        q.append( ((dic1["x"], dic1["m"], dic1["a"], dic1["s"]), (dic2["x"], dic2["m"], dic2["a"], dic2["s"]), name) )
                        break
                    elif dic1[cat] < num:
                        curr = dic2[cat]
                        dic2[cat] = num - 1
                        q.append( ((dic1["x"], dic1["m"], dic1["a"], dic1["s"]), (dic2["x"], dic2["m"], dic2["a"], dic2["s"]), name) )
                        dic2[cat] = curr
                        dic1[cat] = num
                elif ">" in condition:
                    if dic1[cat] > num:
                        q.append( ((dic1["x"], dic1["m"], dic1["a"], dic1["s"]), (dic2["x"], dic2["m"], dic2["a"], dic2["s"]), name) )
                        break
                    elif dic2[cat] > num:
                        curr = dic1[cat]
                        dic1[cat] = num + 1
                        q.append( ((dic1["x"], dic1["m"], dic1["a"], dic1["s"]), (dic2["x"], dic2["m"], dic2["a"], dic2["s"]), name) )
                        dic1[cat] = curr
                        dic2[cat] = num
            else:
                q.append( ((dic1["x"], dic1["m"], dic1["a"], dic1["s"]), (dic2["x"], dic2["m"], dic2["a"], dic2["s"]), eqn) )
                break
    
    for start, end in accepted:
        x1, m1, a1, s1 = start
        x2, m2, a2, s2 = end

        ans += (x2-x1+1) * (m2-m1+1) * (a2-a1+1) * (s2-s1+1)
    
    return ans


for path in [test_path, file_path]:

    ans = 0

    with open(path, 'r') as file:
        workflow, rates = file.read().split('\n\n')

    workflow = workflow.split('\n')
    rates = rates.split('\n')
    
    ratings = []
    # Iterate through each line and parse the values into a dictionary
    for line in rates:
        # Remove leading and trailing curly braces, then split by commas
        parts = line[1:-1].split(',')
        line_dict = {}

        # Iterate through key-value pairs and add them to the dictionary
        for part in parts:
            key, value = part.split('=')
            line_dict[key.strip()] = int(value.strip())

        ratings.append(line_dict)


    work = {}
    # Iterate through each line and extract key-value pairs
    for line in workflow:
        # Extract the key and value parts
        key, value_part = line.split('{')
        key = key.strip()
        value_part = value_part.rstrip('}')
        values = [part.strip() for part in value_part.split(',')]

        work[key] = values


    print("="*80)
    print(part1(work, ratings))
    print(part2(work))
    print("="*80)
