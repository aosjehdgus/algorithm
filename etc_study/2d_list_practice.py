# 연산자 * 로 2중 리스트 선언

print("# 연산자 * 로 2중 리스트 선언")
array = [[0]*2]*3
# array = [[0]*열]*행
print(array)

print("")

# 연산자와 for 문으로 2중 리스트 선언

print("# 연산자와 for 문으로 2중 리스트 선언")
array_1 = [[0]*2 for i in range(3)]
# array_1 = [[0]*열]* for i in range(행)]
print(array_1)

print("")

# 2중 for 문으로 2중 리스트 선언

print("# 2중 for 문으로 2중 리스트 선언")
array_2 = [[0 for col in range(2)] for row in range(3)]
# array_2 = [[0 for col in range(열)] for row in range(행)]
print(array_2)

