day = 20
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


from collections import defaultdict

# def button(connections, type, button_presses):
#     states = {}
#     conjunction_states = {}
#     low_pulses = 0
#     high_pulses = 0

#     for s in type.keys():
#         states[s] = False
#         if type[s] == '&':
#             conjunction_states[s] = []
    
    
#     SEEN = set()
#     seen_time = {}

#     press = 0
#     while press < button_presses:

#         if tuple(states) not in SEEN:
#             SEEN.add(tuple(states))
#         else:
#             press *= button_presses // press
#             low_pulses *= button_presses // press
#             high_pulses *= button_presses // press
        
#         print('\n\n\n\n')

#         pulse_queue = [("button", "low", "broadcaster")]
#         low_pulses += 1
#         while pulse_queue:
            
#             print(states)
#             source, pulse_type, destination = pulse_queue.pop(0)
#             #print(source, pulse_type, destination)
            
#             if type[source] == '%':
#                 if pulse_type == "high":
#                     continue
                
#                 states[source] = not states.get(source, False)
#                 if states[source]:
#                     for next_destination in connections[source]:
#                         pulse_queue.append( (destination, "high", next_destination) )
#                         if type[next_destination] == '&':
#                             conjunction_states[next_destination].append(True)
#                         high_pulses += 1
#                 else:
#                     for next_destination in connections[source]:
#                         pulse_queue.append( (destination, "low", next_destination) )
#                         if type[next_destination] == '&':
#                             conjunction_states[next_destination].append(False)
#                         low_pulses += 1
#             elif type[source] == '&':
#                 if len(conjunction_states[source]) == 1:
#                     states[source] = not conjunction_states[source][0]
#                     if states[source]:
#                         for next_destination in connections[source]:
#                             pulse_queue.append( (destination, "high", next_destination) )
#                             if type[next_destination] == '&':
#                                 conjunction_states[next_destination].append(True)
#                             high_pulses += 1
#                     else:
#                         for next_destination in connections[source]:
#                             pulse_queue.append( (destination, "low", next_destination) )
#                             if type[next_destination] == '&':
#                                 conjunction_states[next_destination].append(False)
#                             low_pulses += 1
#                 else:
#                     if all(conjunction_states[source]):
#                         for next_destination in connections[source]:
#                             pulse_queue.append( (destination, "low", next_destination) )
#                             if type[next_destination] == '&':
#                                 conjunction_states[next_destination].append(False)
#                             low_pulses += 1
#                     else:
#                         for next_destination in connections[source]:
#                             pulse_queue.append( (destination, "high", next_destination) )
#                             if type[next_destination] == '&':
#                                 conjunction_states[next_destination].append(True)
#                             high_pulses += 1
#             else:
#                 for next_destination in connections[source]:
#                     pulse_queue.append( (destination, pulse_type, next_destination) )
#                     if type[next_destination] == '&':
#                             conjunction_states[next_destination].append(False)
#                     if pulse_type == "low":
#                         low_pulses += 1
#                     else:
#                         high_pulses += 1

#         press += 1

#     return low_pulses, high_pulses

from collections import deque
import math

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}
    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"



for path in [file_path]:
    
    #Part 1
    modules = {}
    broadcast_targets = []
    
    for line in open(path):
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"

    lo = hi = 0

    (feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

    cycle_lengths = {}
    seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

    presses = 0


    for _ in range(1000):
        lo += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
        
        while q:
            origin, target, pulse = q.popleft()

            if pulse == "lo":
                lo += 1
            else:
                hi += 1
            
            if target not in modules:
                continue
            
            module = modules[target]
            
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))

    print(lo * hi)


    #Part 2
    modules = {}
    broadcast_targets = []
    
    for line in open(path):
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"

    while True:
        presses += 1
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
        
        while q:
            origin, target, pulse = q.popleft()
            
            if target not in modules:
                continue
            
            module = modules[target]
            
            if module.name == feed and pulse == "hi":
                seen[origin] += 1

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                else:
                    assert presses == seen[origin] * cycle_lengths[origin]
                    
                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = x * cycle_length // math.gcd(x, cycle_length)
                    print(x)
                    exit(0)
            
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
    
    # ans = 0

    # with open(path, 'r') as file:
    #     lines = [line.strip() for line in file.read().split('\n')]

    # connections = {"button": ["broadcaster"]}
    # type = defaultdict(lambda: "None")
    
    # for line in lines:
    #     source, destinations = line.split(' -> ')
    #     destinations = destinations.split(', ')
    #     if not source[0].isalnum():
    #         type[source[1::]] = source[0]
    #         source = source[1::]
    #     connections[source] = destinations
    
    # low, high  = button(connections, type, 1000)
    # print(low, high)

    
    # print("="*80)
    # print(low*high)
    # print("="*80)