from collections import deque

queue = deque()

queue.append(1)
queue.popleft()
queue.append(3)
queue.append(1)
queue.append(13)
queue.popleft()


print(queue)

def bfs (graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = '')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

각 노드가 연결된 정보를 표현 (2차원 리스트)

w, h = map(int, input().split())

graph = []

for i in range(w):

    graph.append(list(map(int, input())))

print(graph)





