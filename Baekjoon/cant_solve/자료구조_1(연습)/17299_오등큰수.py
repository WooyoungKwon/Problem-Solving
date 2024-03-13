import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
count = [0] * 1000001
stack = []
ans = [-1] * N
for i in seq:
    count[i] += 1

for i in range(N):
    while stack and count[seq[i]] > count[seq[stack[-1]]]:
        ans[stack.pop()] = seq[i]
    stack.append(i)
print(*ans)