import sys

N = int(sys.stdin.readline())
deque1 = []
deque2 = []

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push_front':
        deque1.append(command[1])
    elif command[0] == 'push_back':
        deque2.append(command[1])
    elif command[0] == 'pop_front':
        if deque1:
            print(deque1.pop())
        elif deque2:
            print(deque2.pop(0))
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deque2:
            print(deque2.pop())
        elif deque1:
            print(deque1.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque1) + len(deque2))
    elif command[0] == 'empty':
        if deque1 or deque2:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deque1:
            print(deque1[-1])
        elif deque2:
            print(deque2[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if deque2:
            print(deque2[-1])
        elif deque1:
            print(deque1[0])
        else:
            print(-1)