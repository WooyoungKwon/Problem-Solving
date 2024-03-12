import sys

cnt = int(sys.stdin.readline())
stack = []
answer = []
tmp = 1
for i in range(cnt):
    seqNum = int(sys.stdin.readline())
    while(tmp <= seqNum):
        stack.append(tmp)
        answer.append('+')
        tmp += 1
    if(stack[-1] == seqNum):
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        exit()
for i in answer:
    print(i)