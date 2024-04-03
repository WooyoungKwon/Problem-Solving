import sys
def fac(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return n * fac(n-1)

def countZero(n):
    n = str(n)
    cnt = 0
    for i in range(len(n)-1, 0, -1):
        if n[i] != '0':
            break
        elif n[i] == '0':
            cnt += 1
    return cnt


def comb(n, r):
    return fac(n) / fac(r) * (fac(n-r))

n, r = map(int, sys.stdin.readline().split())

print(countZero(comb(n, r)))