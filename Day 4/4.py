day = 4
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"


for path in [test_path, file_path]:

    ans = 0
    sum = 0

    with open(path, 'r') as file:
        lines = file.readlines()
        cards = [1 for i in range(len(lines))]

        for k, card in enumerate(lines):
            card_number, data = card.split(":")
            parts = data.split('|')
            list1 = list(map(int, parts[0].split()))
            list2 = list(map(int, parts[1].split()))

            ans = len(set(list1) & set(list2))

            for i in range(ans):
                cards[k+i+1] += cards[k]

            if ans != 0:
                sum += 2**(ans-1)

    ans2 = 0
    for j in cards:
        # print(j)
        ans2 += j
    print("="*80)
    print(sum, ans2)
    print("="*80)
