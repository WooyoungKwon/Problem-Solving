import sys

# bar = sys.stdin.readline().rstrip()
bar = "(((()(()()))(())()))(()())"
stack = []
ans = 0

for i in range(len(bar)):
    if  bar[i] == "(":
        stack.append("(")
    elif bar[i] == ")":
        if bar[i-1] == "(":
            stack.pop()
            ans += len(stack)
            print(stack)
        else:
            stack.pop()
            ans += 1
print(ans)