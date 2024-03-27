# 시간 복잡도 : O(n^2)
import sys

# S = "baekjoon"
S = sys.stdin.readline().rstrip()
ans = []
for i in range(len(S)):
    ans.append(S[i:])

ans.sort()

for k in ans:
    print(k)