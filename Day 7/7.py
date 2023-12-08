day = 7
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

from collections import Counter

def strength(hand, part2):
    #Since ASCII of alphabets > ASCII of numbers > ASCII of '.
    hand = hand.replace('A','E')
    hand = hand.replace('K','D')
    hand = hand.replace('Q','C')
    hand = hand.replace('J','B' if not part2 else '.')
    hand = hand.replace('T','A')

    C = Counter(hand)

    #Add number of Joker cards to the non-joker card with max occurence
    #Remove joker cards from Counter
    if part2:
        target = list(C.keys())[0]
        for k in C:
            if k!='.':
                if C[k] > C[target] or target=='.':
                    target = k
        assert target != '.' or list(C.keys()) == ['.']
        if '.' in C and target != '.':
            C[target] += C['.']
            del C['.']
        assert '.' not in C or list(C.keys()) == ['.'], f'{C} {hand}'

    #Return (rank, hand) bases on type of hand
    if sorted(C.values()) == [5]:
        return (6, hand)
    elif sorted(C.values()) == [1,4]:
        return (5, hand)
    elif sorted(C.values()) == [2,3]:
        return (4, hand)
    elif sorted(C.values()) == [1,1,3]:
        return (3, hand)
    elif sorted(C.values()) == [1,2,2]:
        return (2, hand)
    elif sorted(C.values()) == [1,1,1,2]:
        return (1, hand)
    elif sorted(C.values()) == [1,1,1,1,1]:
        return (0, hand)
    else:
        assert False, f'{C} {hand} {sorted(C.values())}'


for path in [test_path, file_path]:
    
    with open(path, 'r') as file:
        lines = file.readlines()

        for part2 in [False, True]:
            H = [(line.split()[0], line.split()[1])  for line in lines]
            H = sorted(H, key=lambda hb:strength(hb[0], part2))

            ans = 0

            for i, (hand, bid) in enumerate(H):
                ans += (i+1) * int(bid)
                
            print(ans)
    
    print("="*80)