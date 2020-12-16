from collections import deque

# 큐(Queue) 구현을 위해서 deque 라이브러리 사용

queue = deque()

# 삽입(1) - 삽입(3) -  삭제() - 삽입(2)

queue.append(1)
queue.append(3)
queue.popleft()
queue.append(2)

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력
