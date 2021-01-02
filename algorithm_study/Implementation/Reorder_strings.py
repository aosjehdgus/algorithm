# 알파벳 대문자와 숫자(0 ~9) 로만 구성된 문자열이 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

# 예를 들어, K1KA5CB7 이라는 값이 들어오면 ABCKK13 출력합니다.

data = list(input())

alpha = []
value = 0

for x in data:

    if x.isalpha():
        alpha.append(x)
    
    else :
        value += int(x)

alpha.sort()

if value != 0 :

    alpha.append(str(value))

print(''.join(alpha))


