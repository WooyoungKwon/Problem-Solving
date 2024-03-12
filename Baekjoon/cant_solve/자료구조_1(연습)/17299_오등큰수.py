import sys

# N = int(sys.stdin.readline())
# seq = list(map(int, sys.stdin.readline().split()))
N = 7
seq = 1, 1, 2, 3, 4, 2, 1
count = [0] * 1000001
stack = []
ans = [-1] * N
for i in seq:
    count[i] += 1

for i in range(N):
    while stack and count[seq[stack[-1]]] < count[seq[i]]:
        ans[stack.pop()] = seq[i]
    stack.append(i)
print(ans)
# 1 1 2 3 4 2 1