# 1. 정수 1개 입력 받아 출력

# n = int(input())

# print(n)

# 2. 문자열 1개 입력 받아 출력

#  a = input()

# print(a)

# 3. 정수 2개 입력 받아 출력

# x, y = map(int,input().split())

# print(x, y)

# 4. 문자 2개 입력 받아 출력 순서 바꿔 출력하기

# x, y = input().split()

# print(y, x)

# 5. 실수 1개 입력 받아 그대로 출력하기

# a = input()

# print(a)

# 6. 실수 1개 입력받아 둘째 자리까지 출력하기(다시)

# a = input()
# b = str(round(a,2))
# print(b)

# 7. 정수 1개 입력받아 3번 출력하기

# a = input()

# print(a, a, a)

# 8. 시간 입력받아 그대로 출력하기

# h, m = map(int,input().split(':'))

# print(str(h) + ":" + str(m))

# 9. 연월일 입력받아 그대로 출력하기

# y, m, d = map(int, input().split("."))

# if y < 100:
#     y = "19" + str(y) 
#     print(str(y).zfill(4) + "." + str(m).zfill(2) + "." + str(d).zfill(2))

# else:
#     print(str(y).zfill(4) + "." + str(m).zfill(2) + "." + str(d).zfill(2))



# y, m, d = map(int, input().split("."))
 
# print(str(y).zfill(4) + "." + str(m).zfill(2) + "." + str(d).zfill(2))

# 10. 주민번호 입력받아 형태 바꿔 출력하기

# x, y = input().split('-')

# print(x + y)

# 11. 단어 1개 입력받아 그대로 출력하기

# a = input()

# print(a)

# 12. 실수 1개 입력받아 부분별로 출력하기

# a = input().split(".")

# print(a[0])
# print(a[1])

# 13. 단어 1개 입력받아 나누어 출력하기

# a = input()
# a = list(a)
# b = len(a)


# for i in range(b):
#     print("'"+ a[i] + "'")

# 14. 정수 1개 입력받아 나누어 출력하기

# a = int(input())

# b = (a // 10000) * 10000
# c = (a // 1000) * 1000 - (a // 10000) * 10000
# d = (a // 100) * 100 - (a // 1000) * 1000
# e = (a // 10) * 10 - (a // 100) * 100
# f = (a // 1) * 1 - (a // 10) * 10

# array = [10000, 1000, 100, 10, 1]
# k = len(array)

# for i in array:

#     b = (a // i) * i

# b = (a // 10000) * 10000
# b + c = (a // 1000) * 1000
# b + c + d = (a // 100) * 100
# b + c + d + e = (a // 10) * 10
# b + c + d + e + f = (a // 1) * 1

# (a // 10000) * 10000 + c = (a // 1000) * 1000
# (a // 1000) * 1000 + d = (a // 100) * 100
# (a // 100) * 100 + e = (a // 10) * 10
# (a // 10) * 10 + f = (a // 1) * 1


# print("[" + str(b) + "]" ,
#       "[" + str(c) + "]" ,
#       "[" + str(d) + "]" ,
#       "[" + str(e) + "]" ,
#       "[" + str(f) + "]", sep = '\n')

# 15. 시분초 입력받아 분만 출력하기

# a, b, c = map(int, input().split(":"))

# print(b)

# 16. 년월일 입력 받아 형식 바꿔 출력하기

# y, m, d = map(int, input().split("."))

# print(str(d).zfill(2) + "-" + str(m).zfill(2) + "-" + str(y).zfill(4))

# 17.  정수 1개 입력받아 그대로 출력하기2

# a = input()

# print(a)

# 18. 실수 1개 입력받아 그대로 출력하기2 안됨

# a = input()
# a = float(a)
# a = round(a, 11)

# print(a)

# 19. 10진 정수 1개 입력받아 8진수로 출력하기


# 슬라이싱 해서 출력하기

# a = input()
# b = oct(int(a))[2:]

# print(b)

# # 시간 21 코드 길이 44B


# c = input() 
# c = format(int(c), 'o')

# print(c)

# 시간 23 코드 길이 49B

# 포맷 보다 슬라이싱이 더 적은 메모리에, 빠르게 처리된다.


# 1033 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2(설명)

# a = input()

# a = hex(int(a))[2:]
# print(a.upper())  

# 1034 : [기초-출력변환] 8진 정수 1개 입력받아 10진수로 출력하기(설명)

# a = input()

# b = int('0o' + a, 8)

# print(b)

# 1035 : [기초-출력변환] 16진 정수 1개 입력받아 8진수로 출력하기(설명)

# a = input()

# b = int('0x' + a, 16)
# c = format(b, 'o')

# print(c)

# 1036 : [기초-출력변환] 영문자 1개 입력받아 10진수로 출력하기(설명)

# a = input()

# print(ord(a))

# 1037 : [기초-출력변환] 정수 입력받아 아스키 문자로 출력하기

# a = input()
# a = int(a)

# print(chr(a))

# 1038 : [기초-산술연산] 정수 2개 입력받아 합 출력하기1(설명)

# a, b = map(int, input().split(" "))

# print(a + b)


# 1040 : [기초-산술연산] 정수 1개 입력받아 부호 바꿔 출력하기(설명)


# a = input()
# print(int(a) * -1)


# 1041 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)

# x = input()
# y = ord(x) + 1

# print(chr(y))

# 1042 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 출력하기(설명)

# x, y = map(int, input().split(" "))

# print(x // y)

# 1045 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기 (답이 이상함)
# x, y = map(int, input().split(" "))

# print(x + y)
# print(x - y)
# print(x * y)
# print(x // y)
# print(x % y)
# print(float(round(x / y, 2)))

# 1046 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기

# x, y, z = map(int, input().split())

# sum = x + y + z 
# avg = sum / 3
# print(sum)
# print(round(avg,1))


# f = list(map(int, input().split()))
# print(f)

# import sys

# data = sys.stdin.readline().rstrip()

# print(data)


