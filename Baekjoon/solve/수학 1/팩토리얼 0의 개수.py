import sys
def fac(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return n * fac(n-1)

N = int(sys.stdin.readline())

facN = str(fac(N))
cnt = 0
for i in range(len(facN)-1, 0, -1):
    if facN[i] != '0':
        break
    elif facN[i] == '0':
        cnt += 1

print(cnt)