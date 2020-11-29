n, k = map(int, input().split())

# N을 K로 나누었을 때, 나누어 떨어지면 실행

# 나누어 떨어지지 않으면 -1 

# result는 연산을 하는 총 횟수
result = 0

while True:
    # n이 k로 나누어 떨어지지 않을 때, 가장 가까운 k로 나누어 떨어지는 수가 무엇인지 찾고자 할 때 사용
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출  
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

result += (n - 1)
print(result)