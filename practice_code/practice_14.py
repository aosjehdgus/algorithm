# # 1099 : [기초-2차원배열] 성실한 개미

# # 영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

# # 왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
# # 그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

# # 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
# # (오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

# # 이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

# # 미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
# # 오른쪽 또는 아래쪽으로만 움직였다.

# # 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# # 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

# # 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
# # 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

# # 미로 상자의 테두리는 모두 벽으로 되어 있으며,
# # 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

# # 입력
# # 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.


# # 출력
# # 성실한 개미가 이동한 경로를 9로 표시해 출력한다.


# # 입력 예시   
# # 1 1 1 1 1 1 1 1 1 1
# # 1 0 0 1 0 0 0 0 0 1
# # 1 0 0 1 1 1 0 0 0 1
# # 1 0 0 0 0 0 0 1 0 1
# # 1 0 0 0 0 0 0 1 0 1
# # 1 0 0 0 0 1 0 1 0 1
# # 1 0 0 0 0 1 2 1 0 1
# # 1 0 0 0 0 1 0 0 0 1
# # 1 0 0 0 0 0 0 0 0 1
# # 1 1 1 1 1 1 1 1 1 1

# # 출력 예시
# # 1 1 1 1 1 1 1 1 1 1
# # 1 9 9 1 0 0 0 0 0 1
# # 1 0 9 1 1 1 0 0 0 1
# # 1 0 9 9 9 9 9 1 0 1
# # 1 0 0 0 0 0 9 1 0 1
# # 1 0 0 0 0 1 9 1 0 1
# # 1 0 0 0 0 1 9 1 0 1
# # 1 0 0 0 0 1 0 0 0 1
# # 1 0 0 0 0 0 0 0 0 1
# # 1 1 1 1 1 1 1 1 1 1


# from collections import deque

# # 개미가 이동할 수 있는 방향 오른쪽, 아래

# dx = [1,0]
# dy = [0,1]

# # graph 만들기

# graph = []
# for i in range(10):
#     graph.append(list(map(int,input().split())))
   
# # 개미집 표시

# graph[1][1]=9

# print(bfs(1,1))


# # BFS 소스코드 구현
# def bfs (x, y):
# # 큐(Queue) 구현을 위해서 deque 라이브러리 선언
#     queue = deque()
#     queue.append((x,y))
#     # 큐가 빌 때까지 진행
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 두가지 방향 확인
#         for i in range(2):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 구역을 벗어난 경우 무시
#             if nx < 1 or nx > 8 ny < 1 or ny > 8:
#                 continue
#             # 벽을 만난 경우 
#             if graph[nx][ny] == 1:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 9표시
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = 9
#             # 먹이를 찾은 경우나 움직일 수 없거나 맨 아래쪽에 도착한 경우 멈춤
#             if graph[nx][ny] == 2:
#                 graph[nx][ny] = 9
#                 queue.append((nx,ny))
#             # 움직일 수 없는 경우
#             elif graph[x+1][y] == 1 and graph[x][y+1] == 1:
#                 graph[nx][ny] = 9
#                 queue.append((nx,ny))
#             # 맨 아래쪽에 도착한 경우
#             elif nx == 8 and ny == 8:
#                 graph[nx][ny] = 9
#                 queue.append((nx,ny))


#     return()


# 개미가 이동할 수 있는 방향 오른쪽, 아래
dx = [1,0]
dy = [0,1]

# graph 만들기
graph = []
for i in range(10):
    graph.append(list(map(int,input().split())))

# 개미집 표시
graph[1][1]=9

def abc(x,y):
    while True:
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            # 구역을 벗어난 경우 무시
            if nx < 1 or nx > 8 or ny < 1 or ny > 8:
                continue
            # 벽을 만난 경우 
            if graph[nx][ny] == 1:
                continue
            # 해당 노드를 처음 방문하는 경우에만 9표시
            if graph[nx][ny] == 0:
                graph[nx][ny] = 9
            # 먹이를 찾은 경우나 
            if graph[nx][ny] == 2:
                graph[nx][ny] = 9
                            
            # 움직일 수 없는 경우
            elif graph[x+1][y] == 1 and graph[x][y+1] == 1:
                graph[nx][ny] = 9
            
            # 맨 아래쪽에 도착한 경우
            elif nx == 8 and ny == 8:
                graph[nx][ny] = 9
    return(graph)         


print(abc(1,1))
