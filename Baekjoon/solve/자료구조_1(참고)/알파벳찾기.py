import sys

S = list(sys.stdin.readline().rstrip())
count = [-1 for _ in range(26)]

L = len(S)

for i in range(L):
    idx = ord(S[i]) - 97
    print(idx)
    if count[idx] == -1:
        count[idx] += i+1

print(*count)