# 2020.12.14(월)

# 1070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기

# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

# 입력 예시

# 12

# 출력 예시

# winter

# month = int(input())

# if month == 12 or month == 1 or month ==  2 : 
#     print('winter')
# elif month == 3 or month == 4 or month == 5 : 
#     print('spring')
# elif month == 6 or month == 7 or month == 8 :
#     print('summer')
# elif month == 9 or month == 10 or month == 11 :
#     print('fall')

# 1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1(다시하기)

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.

# number = input().split()

# for i in range(len(number)) :
    
#     if number[i] == "0" :

# 1072 : [기초-반복실행구조] 정수 입력받아 계속 출력하기

# n = int(input())
# data = input().split()

# for i in range(n):
#     print(data[i])
        

# 1073 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기2(다시 하기)


# data = input().split()

# for i in range(len(data)):

#     if data[i] == 0:

#         data[i] = data[i-1]

#         print(data[i])

# while data == 0:

#     print(data)

#    print(data[i])

#         if data[i] == 0:

#             break
        
# 1074 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1

# <입력 예시>
# 5

# <출력 예시>
# 5
# 4
# 3
# 2
# 1

# n = int(input())


# while n > 0 :

#     print(n)
#     n = n-1
    
# 1075 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2     
        
# n = int(input())

# while n > 0  :
    
#     n = n-1
#     print(n)
    
    
    
    
        




