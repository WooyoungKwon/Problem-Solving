import sys

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
N = int(sys.stdin.readline())
numList = map(int, sys.stdin.readline().rstrip().split())
count = 0
for i in numList:
    if isPrime(i):
        count += 1

print(count)