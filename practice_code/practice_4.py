# 2020년 12월 12일(토)

# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기

# a, b, c = map(int, input().split())

# if a % 2 == 0 :
#    print(a)

# if b % 2 == 0 :
#    print(b)

# if c % 2 == 0 :
#    print(c)


# 1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기

# a, b, c = map(int, input().split())

# if a % 2 == 0 :
#     print("even")

# else :
#     print("odd")

# if b % 2 == 0 :
#     print("even")

# else :
#     print("odd")

# if c % 2 == 0 :
#     print("even")

# else :
#     print("odd")


# 1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기
# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

# a = input()

# if int(a) > 0 :
#     print("plus")

#     if int(a) % 2 == 0 :
#         print("even")

#     else :
#         print("odd")

# else :
#     print("minus")

#     if int(a) % 2 == 0 :
#         print("even")

#     else :
#         print("odd")

# 1068 : [기초-조건/선택실행구조] 정수 1개 입력받아 평가 출력하기
# # 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

# a = input()

# if 90 <= int(a) <= 100:
#     print("A")

# if 70 <= int(a) <= 89:
#     print("B")

# if 40 <= int(a) <= 69:
#     print("C")

# if 0 <= int(a) <= 39:
#     print("D")

# 1069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

# a = input()
 
# if a == "A" :
#     print("best!!!")
# elif a == "B" :
#     print("good!!")
# elif a == "C" :
#     print("run!")
# elif a == "D" :
#     print("slowly~")
# else :
#     print("what?")
    


