import sys

# 에라토스테네스의 체
isPrime = [True] * 1000001
for i in range(2, 1001): # 1000까지만 모든 수를 반복해서 소수를 찾으면 된다.
    if isPrime:
        for j in range(i + i, 1000001, i): # 2와 3은 어차피 소수, 4는 2로 만들어짐, 5도 소수 <- 이런 방식이기 때문에 i + i로 체를 더 빨리 만든다.
            isPrime[j] = False


while True:
    n = int(sys.stdin.readline())
    flag = True # 입력받은 수를 소수의 합으로 나타 낼 수 없는 경우, 주어진 문장을 출력하기 위한 변수
    if n == 0:
        break
    for k in range(3, n, 2):
        if isPrime[k] and isPrime[n-k]: # 'n = 소수(k) + 소수(n-k)'이어야 함으로 두 수가 모두 소수인지 판별
            if n-k == 1 or (n-k)%2 == 0: # n이 4일 경우 k가 3일 때 n-k는 1이 된다. 1은 소수가 아니기 때문에 n-k가 1일 경우를 잡아준다.
                continue
            print(f"{n} = {k} + {n-k}")
            flag = False
            break
    if flag:
        print("Goldbach's conjecture is wrong.")