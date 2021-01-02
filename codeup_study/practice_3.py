# 1059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기

# a = input()

# print(~int(a))


# 1060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기

# a, b = map(int, input().split())

# print(a & b)

# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기

# a, b = map(int, input().split())

# print(a if a>b else b)

# 1064 : [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기

# a, b, c = map(int, input().split())

# min = a if b > a else b 
# min = min if c > min else c

# print(min)

# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기

a, b, c = map(int, input().split)

if a % 2 == 0 :
   print(a)

if b % 2 == 0 :
   print(b)

if c % 2 == 0 :
   print(c)