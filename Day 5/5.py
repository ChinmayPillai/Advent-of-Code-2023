day = 5
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

def apply_map(value, mapping):
    for dest_start, source_start, length in mapping:
        if value >= source_start and value < source_start + length:
            return dest_start + (value - source_start)
    return value

def map_seeds_to_location(seed, *maps):
    for mapping in maps:
        seed = apply_map(seed, mapping)
    return seed

def find_lowest_location(seeds, *maps):
    lowest_location = float('inf')
    for k, seed in enumerate(seeds):
        location = map_seeds_to_location(seed, *maps)
        lowest_location = min(lowest_location, location)
        #print("seed ", k)
    return lowest_location

for path in [test_path, file_path]:
    
    ans = 0
    sum = 0

    with open(path, 'r') as file:
        lines = file.read()
        sections = lines.strip().split('\n\n')
        seeds = list(map(int, sections[0].split()[1:]))
        maps = [[list(map(int, line.split())) for line in section.strip().split('\n')[1:]] for section in sections[1:]]

        #for i in range(0, len(seeds), 2):
            # newseeds = []
            # print("set", i//2, "of", len(seeds)//2)
            # for j in range(seeds[i], seeds[i]+seeds[i+1]):
            #     newseeds.append(j)
        
            # print("number of seeds: ", len(newseeds))
            
            # Find the lowest location among seeds
        lowest_location = find_lowest_location(seeds, *maps)
            #ans = min(lowest_location, ans)

    
    print("="*80)
    print(lowest_location)
    print("="*80)