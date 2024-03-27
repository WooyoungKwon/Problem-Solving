import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
mul = A * B
while True:
    r = A % B
    if r == 0:
        # 최대공약수
        print(B)
        break
    A = B
    B = r
# 최소공배수
print(mul//B)