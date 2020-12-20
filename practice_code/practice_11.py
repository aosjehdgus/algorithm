# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기1

# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

# 입력
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.


# 출력
# 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.


# 입력 예시   
# 10
# 1 3 2 2 5 6 7 4 5 9

# 출력 예시
# 1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0

#

# 

# 5번 무작위로 불렀을 때, 

# 5

# 1 4 2 2 1

# 2 2 0 1 0 0 0 0 0 0 0 0 ..
# n_list = []
# result_list = []

# for i in range(1,24):

#     i = str(i)
#     n_list.append(i)

# n = input()
# number = list(map(str, input().split()))

# for j in number:

#     result = n_list.count(j)

# result_list.append(result)

# print(result_list)

# # print(n_list.count('2'))



# 1094 : [기초-1차원배열] 이상한 출석 번호 부르기2

# n = int(input())
# number = list(map(int, input().split()))

# number.reverse()

# for i in range(n):
#     print(number[i], end=' ')

# 1095 : [기초-1차원배열] 이상한 출석 번호 부르기3
# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

# n = input()
# number = list(map(int, input().split()))

# print(min(number))













    
