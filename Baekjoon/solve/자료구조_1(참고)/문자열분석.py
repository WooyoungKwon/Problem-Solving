import sys

S = list(sys.stdin.readline().rstrip())
rot13 = ''

for i in range(len(S)):
    asc = ord(S[i])
    # 대문자일 경우
    if 64 < asc < 91:
        rotNum = asc + 13
        # 만약 90를 넘어가면 넘어간만큼 64부터 다시 카운트
        if rotNum > 90:
            rotNum = 64 + (rotNum - 90)
        rot13 += chr(rotNum)

    # 소문자일 경우
    elif 96 < asc < 123:
        rotNum = asc + 13
        # 만약 122를 넘어가면 넘어간만큼 96부터 다시 카운트
        if rotNum > 122:
            rotNum = 96 + (rotNum - 122)
        rot13 += chr(rotNum)
    else:
        rot13 += S[i]
print(rot13)