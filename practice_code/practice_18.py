# 1151 : 10보다 작은 수

# 10보다 작은 수가 입력되면 small 을 출력, 10이상이면 아무것도 출력하지 마시오.

# n = int(input())


# if n < 10 :
#     print("small")


# 1152 : 10보다 작은 수 (else 버전)

# 10보다 작은 정수가 입력되면 small 을 출력, 그 이상의 수가 입력되면 big 을 출력하시오.


# n = int(input())

# if n < 10 :
#     print("small")
# else :
#     print("big")

# 1153 : 두 수의 대소 비교

# 두 정수가 입력된다.  두 정수의 크기를 비교하여 왼쪽 수가 크면 > 를 출력, 
# 오른쪽 수가 크면 < 를 출력, 같으면 = 을 출력하시오.

# a, b = map(int, input().split())

# if a > b :
#     print(">")
# elif a == b :
#     print("=")
# else :
#     print("<")

# 1154 : 큰수 - 작은수
    
# 정수 두개가 입력으로 들어오면 큰수 - 작은수의 값을 출력하시오.

# a, b = map(int, input().split())

# if a >= b :

#     print(a-b)

# else : 

#     print(b-a)

# 1155 : 7의 배수

# 인학이는 숫자 7을 좋아한다.

# 어떤 정수가 입력되면 그 수가 7의 배수인지 확인하시오.

# n = int(input())

# if n % 7 == 0 :
#     print("multiple")

# else : 
#     print("not multiple")

# 1156 : 홀수 짝수 구별

# 어떤 자연수가 입력되면  홀수이면 "odd"을 출력하고, 짝수이면 "even"을 출력하시오.

# n = int(input())

# if n % 2 == 0 :
#    print("even")
# else :
#     print("odd") 

# 1157 : 특별한 공 던지기 1

# 슬기가 던진 공의 위치가 입력으로 주어지면 50이상 60이하이면 
# "win"을 출력하고, 그 외에는 "lose"를 출력하시오.


n = input()

if n >= str(50) and n <= str(60) :
    print("win")

else : 
    print("lose")