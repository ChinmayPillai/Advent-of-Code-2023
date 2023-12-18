day = 18
file_path = "Day " + str(day) + "/" + str(day) + ".txt"
test_path = "Day " + str(day) + "/test.txt"

translation_table = str.maketrans("", "", "()")


# Shoelace formula
# Area = abs(Sum(xi * (yi-1 - yi+1) )) / 2
# where xi, yi are corners of polygon
# - but points on matrix are within the actual polygon bounday, loose some area
# Pick's Formula
# Area = #interior pts + #boundary pts/2 - 1
# =>  #interior pts = Area - #boundary pts/2 + 1
# Total Area = #interior pts + #boundary pts


dir = {
    "U": (-1, 0),
    "L": (0, -1),
    "D": (1, 0),
    "R": (0, 1),
}

dir2 = {
    3: (-1, 0),
    2: (0, -1),
    1: (1, 0),
    0: (0, 1),
}


def decode_col(colour):
    hex = colour[1:-1]
    d = int(colour[-1])

    num = 0

    for ch in hex:
        num *= 16
        if ch.isdigit():
            num += int(ch)
        else:
            num += ord(ch) - ord('a') + 10

    return num, d


for path in [test_path, file_path]:
    print("="*80)

    ans = 0

    with open(path, 'r') as file:
        lines = [line.split(' ') for line in file.read().split('\n')]

    for i in range(len(lines)):
        lines[i][2] = lines[i][2].translate(translation_table)


    for p2 in [False, True]:

        pts = [(0, 0)]
        x, y = 0, 0
        b_pts = 0
        for d, n, colour in lines:

            num, direc = decode_col(colour)

            if not p2:
                dx, dy = dir[d]
                num = int(n)
            else:
                dx, dy = dir2[direc]

            b_pts += num
            x += dx * num
            y += dy * num
            pts.append((x, y))

        area = abs(sum(pts[i][0] * (pts[i-1][1] - pts[(i+1) %
                                                      len(pts)][1]) for i in range(len(pts))))//2

        int_pts = area - b_pts//2 + 1

        ans = int_pts + b_pts

        print(ans)

    print("="*80)
