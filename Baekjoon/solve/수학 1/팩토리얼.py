import sys
def fac(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return n * fac(n-1)

N = int(sys.stdin.readline())

print(fac(N))