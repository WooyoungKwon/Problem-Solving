import sys

N = int(sys.stdin.readline())
post = sys.stdin.readline().rstrip()
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
stack = []

for i in range(len(post)):
    if "A" <= post[i] <= "Z":
        stack.append(num[ord(post[i]) - 65])
    else:
        val1 = stack.pop()
        val2 = stack.pop()
        if post[i] == "+":
            stack.append(val2 + val1)
        elif post[i] == "-":
            stack.append(val2 - val1)
        elif post[i] == "*":
            stack.append(val2 * val1)
        elif post[i] == "/":
            stack.append(val2 / val1)
print("%.2f" %stack[0])