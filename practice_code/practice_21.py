# 1251 : 1 부터 100까지 출력하기

# 1부터 100까지 공백으로 띄워 하나씩 출력한다.


# for i in range(1,101):
#     print(i, end =" ")


# 1252 : 1 부터 n 까지 출력하기

# 문제 설명    
# 어떤 수 n을 입력으로 받아 1부터 n까지의 숫자를 출력하시오.

# 입력
# n이 입력으로 들어온다. (1 <= n <= 100000)

# 출력
# 1부터 n까지 공백으로 띄워 출력한다.

# 입력 예시   
# 5

# 출력 예시
# 1 2 3 4 5 

# n = int(input())

# for i in range(1,n+1):
#     print(i, end=" ")

# 1253 : a 부터 b까지 출력하기

# 문제 설명    
# 어떤 두 수 a, b가 있을 때 두 수 사이의 모든 정수를 오름차순으로 출력하시오.

# 예를 들어, a=5 , b=10일 경우 5 6 7 8 9 10입니다.

# 입력
# 두 수 a, b가 입력으로 들어온다. ( a, b는 정수, a, b 중 어떤 수가 큰지 모름)

# 출력
# a와 b 사이의 정수들을 오름차순으로 출력한다.

# 입력 예시   
# 3 8

# 출력 예시
# 3 4 5 6 7 8 

# a, b = map(int, input().split())

# if a < b :
#     for i in range(a, b+1):
#         print(i, end=" ")
# else : 
#     for i in range(b, a+1):
#         print(i, end=" ")

# 1254 : 알파벳 출력하기

# 문제 설명    
# 시작 알파벳과 마지막 알파벳을 입력받아 그 두 알파벳 사이의 모든 알파벳을 출력하시오.

# 예)

# a f   ====> a b c d e f  

# 입력
# 시작 알파벳과 마지막 알파벳을 공백으로 띄워 입력받는다.(소문자만 입력되고, 사전순으로 입력된다.)

# 출력
# 두 알파벳 사이의 모든 알파벳을 출력한다.

# 입력 예시   
# d g

# 출력 예시
# d e f g 

# x, y = input().split()
# x = ord(x)
# y = ord(y)

# for i in range(x, y+1):
#     print(chr(i), end=" ")

# 1255 : 두 실수 사이 출력하기

# 문제 설명    
# 소수 둘째 자리의 두 실수 a와 b가 입력으로 주어진다.

# a와 b사이의 수를 0.01간격으로 오름차순으로 출력하시오.

# 예)

# 5.67 5.73  ==> 5.67 5.68 5.69 5.70 5.71 5.72 5.73

# 입력
# 두 실수 a와 b가 입력된다. (a <= b) 

# (a,b 중 어떤 수가 큰지 모름) 문제수정 2012.9.20

# 출력
# a와 b사이의 수를 0.01간격으로 오름차순으로 출력하시오.

# 입력 예시   
# 2.00 2.03

# 출력 예시
# 2.00 2.01 2.02 2.03 

# a, b = map(float, input().split())

# if a < b:
#     n = (b - a)//0.01
    
#     for i in range(int(n)+2):
        
#         print("%.2f"% a, end = " ")
#         a = a + 0.01
# elif a == b:
#     print(a)
# else :
#     n = (a - b)//0.01
    
#     for i in range(int(n)+2):
        
#         print("%.2f"% b, end = " ")
#         b = b + 0.01



