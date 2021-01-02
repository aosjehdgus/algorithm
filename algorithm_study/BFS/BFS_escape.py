# <문제> 미로 탈출

# 첫째 줄에 두 정수 n, m이 주어진다. 다음 n개의 줄에는 각각 m개의 정수(0 or 1) 로 미로의 정보가
# 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로제시된다. 또한 시작칸과 마지막 칸은 항상 1이다.

# 첫째 줄에 최소 이동 칸의 개수를 출력한다.

from collections import deque

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):

    graph.append(list(map(int, input())))


# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현

def bfs(x, y):
    
    # 큐(queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]     


# BFS 수행 결과 출력

print(bfs(0,0))


