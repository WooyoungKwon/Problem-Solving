import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
NGE = [-1]*N
stack = []

for i in range(N):
    while stack and num[stack[-1]] < num[i]:
        NGE[stack.pop()] = num[i]
    stack.append(i)
print(*NGE)