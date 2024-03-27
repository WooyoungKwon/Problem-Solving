import sys

ABCD = list(sys.stdin.readline().split())
print(ABCD)
print(int(ABCD[0] + ABCD[1]) + int(ABCD[2] + ABCD[3]))
# S = list("A B C D")
# 1, 5번째 공백
# ABCD.pop(1)
# ABCD.pop(4)
# print(ABCD)