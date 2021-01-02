# 1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기

# 입력
# 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
# 둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
# n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 같은 좌표는 입력되지 않는다.


# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.


# 출력
# 흰 돌이 올려진 바둑판의 상황을 출력한다.
# 흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.

# 입력 예시   
# 5
# 1 1
# 2 2
# 3 3
# 4 4
# 5 5

# 출력 예시
# 1(1,1) 0(1,2) 0(1,3) 0(1,4) 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0(2,1) 1(2,2) 0(2,3) 0(2,4) 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0(3,1) 0(3,2) 1(3,3) 0(3,4) 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0(4,1) 0(4,2) 0(4,3) 1(4,4) 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0(5,1) 0(5,2) 0(5,3) 0(5,4) 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# n = int(input())
# white = []
# graph_2 = [[0 for col in range(19)] for row in range(19)]

# for i in range(n):
    
#      white.append(list(map(int,(input().split()))))

# for j in range(n):

#     x = white[j]
#     x = x[0]
#     y = white[j]
#     y = y[1]
#     graph_2[x-1][y-1] = 1

# for a in graph_2:
#     for b in a:
#         print(b, end=" ")

#     print()

# graph = []
# graph = [[0]*19]*19

# graph_1 = []
# graph_1 = [[0]*19 for i in range(19)]


# 1097 : [기초-2차원배열] 바둑알 십자 뒤집기


graph = []

for i in range(19):

    graph.append(list(map(int, input().split())))

n = int(input())

ten = []

for j in range(n):

    ten.append(list(map(int,input().split())))

for k in range(n):
    
    x = ten[k]
    x = x[0]
    y = ten[k]
    y = y[1]

    for a in range(19):
        
        if graph[a][y-1] == 1:

            graph[a][y-1] = 0
        
        elif graph [a][y-1] == 0:

            graph[a][y-1] = 1 


    for b in range(19):
        
        if graph[x-1][b] == 1:

            graph[x-1][b] = 0
        
        elif graph [x-1][b] == 0:

            graph[x-1][b] = 1 


for e in graph:
    for d in e:
        print(d, end=" ")

    print()





#     graph[0][y] ~ graph[19][y]

# graph[x][0] ~ graph[x][19]







