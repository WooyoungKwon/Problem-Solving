import sys

# f = open("testcase.txt", 'r')
# commands = f.readlines()

cnt = int(sys.stdin.readline())
queue = []

for i in range(cnt):
# for command in commands:
#     command = command.strip().split()
    command = sys.stdin.readline().rstrip().split()
    if not command:
        break
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        if queue:
            print(len(queue))
        else:
            print(0)
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
# f.close()