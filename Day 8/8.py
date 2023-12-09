day = 8
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"
test_path2 = "Day " + str(day) + "/test2.txt"


def lcm(numbers):
    if not numbers:
        return 1
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = lcm_result * num // gcd(lcm_result, num)
    
    return lcm_result

def parse_input(input_str):
    lines = input_str.strip().split('\n')
    nodes = {}
    for i in range(0, len(lines)):
        node_name = lines[i].strip().split(' = ')[0]
        left, right = lines[i].strip().split(' = ')[1][1:-1].split(', ')
        nodes[node_name] = (left, right)
    return nodes


def count_steps_to_ZZZ(nodes, start_node, ins):
    current_node = start_node
    steps = 0
    while current_node != 'ZZZ':
        for i in range(len(ins)):
            steps += 1
            direction = 1 if ins[i] == 'R' else 0
            current_node = nodes[current_node][direction]
    return steps

def count_steps(nodes, start_nodes, ins):
    current_nodes = start_nodes
    step_arr = []
    for current_node in current_nodes:
        steps = 0
        while current_node[-1] != 'Z':
            steps += len(ins)
            for i in range(len(ins)):
                direction = 1 if ins[i] == 'R' else 0
                current_node = nodes[current_node][direction]
        
        step_arr.append(steps)
        #print(steps)
    
    return lcm(step_arr)
    
    
for path in [file_path]:

    with open(path, 'r') as file:
        lines = file.read()

        input_sections = lines.split('\n\n')
        lr_instructions = input_sections[0]
        network_structure = input_sections[1]

        nodes = parse_input(network_structure)
        start_node = "AAA"
        start_nodes = []
        for key in nodes.keys():
            if key[-1] == 'A':
                start_nodes.append(key)
        print(start_nodes)
        steps_to_ZZZ = count_steps_to_ZZZ(nodes, start_node, lr_instructions)
        steps = count_steps(nodes, start_nodes, lr_instructions)

    print("="*80)
    print(steps_to_ZZZ, steps)
    print("="*80)
