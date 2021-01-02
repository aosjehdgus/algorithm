stack = []

stack.append(3)
stack.append(1)
stack.append(4)
stack.append(2)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack)       # 최하단 원소부터 출력