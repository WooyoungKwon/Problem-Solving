import sys

N, K = map(int, sys.stdin.readline().split())
yose = [_ for _ in range(1, N+1)]
answer = []
tmp = K - 1
while yose:
    if tmp >= len(yose):
        tmp = tmp - len(yose)
        continue
    answer.append(yose.pop(tmp))
    tmp += K - 1

print('<', end='')
for i in range(len(answer)):
    print(answer[i], end='')
    if i != len(answer)-1:
        print(end=', ')
print('>')