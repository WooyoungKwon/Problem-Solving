import sys

str1 = list(sys.stdin.readline().rstrip())
cnt = int(sys.stdin.readline())
str2 = []

for i in range(cnt):
    command = sys.stdin.readline().rstrip()
    if command[0] == 'L':
        if str1:
            str2.append(str1.pop())
    if command[0] == 'D':
        if str2:
            str1.append(str2.pop())
    if command[0] == 'B':
        if str1:
            str1.pop()
    if command[0] == 'P':
        str1.append(command[2:])
str2.reverse()
print(''.join(str1+str2))