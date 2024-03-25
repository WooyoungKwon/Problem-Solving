import sys

while True:
    S = list(sys.stdin.readline().strip('\n'))
    if not S:
        break
    count = [0 for _ in range(4)]

    while S:
        asc = ord(S.pop())
        if 96 < asc < 123:
            count[0] += 1
        elif 64 < asc < 91:
            count[1] += 1
        elif asc == 32:
            count[3] += 1
        else:
            count[2] += 1
    print(*count)