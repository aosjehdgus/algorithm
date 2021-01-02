# 1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.


# 입력
# 영문자 1개가 입력된다.
# (a ~ z)


# 출력
# a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.


# 입력 예시   
# f

# 출력 예시
# a b c d e f

# a = ord('z')

# 98 -122

# a 입력시 97
# b 입력시 97 98
# c 입력시 97 98 99
# print(a)

# n = input()
# x = ord(n)

# if x == 97:

#     print(chr(x))

# elif x > 97 : 



#     for i in range(x):

#         print()


# 1077 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

# n = input()

# for i in range(int(n)+1):

#     print(i)


# 1078 : [기초-종합] 짝수 합 구하기

# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# n = input()
# data = int(n)
# count = 0

# for i in range(data + 1):
    
#     if i % 2 == 0:
#         count = count + i

# print(count)

# 1079 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기


# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# a = input().split()

# for data in a :

#     if data != 'q':

#         print(data)

#     else :

#         print(data)
#         break

# 1080 : [기초-종합] 언제까지 더해야 할까?

# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지
# 계속 더하는 프로그램을 작성해보자.


# n = int(input())
# count = 0
# result = 0

# for i in range(n):

#     i += 1
#     count = count + i

#     if count <= n :       

#         print(i)

# print(i)


