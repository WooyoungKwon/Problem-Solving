import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
mul = A * B
while True:
    r = A % B
    if r == 0:
        print(B)
        break
    A = B
    B = r
print(mul//B)