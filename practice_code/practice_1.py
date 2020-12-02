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

a = input()

b = (a // 10000) * 10000 


