import sys

cnt = int(input())
for _ in range(cnt):
    str = sys.stdin.readline().rstrip().split()
    for word in str:
        print(word[::-1])