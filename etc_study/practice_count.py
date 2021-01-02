

dongle = ['1','2','3']  

print(dongle.count('1'))          # 출력 값 1


dongri = ['1','1','1','3','2']    # 출력 값 3

print(dongri.count('1'))


dongle2 = '11234567777'

# 1 1 2 3 4 5 6 7 7 7 7   에서 index를 표기해보면
# 0 1 2 3 4 5 6 7 8 9 10  이다.

print(dongle2.count('1', 0, 1))   # 출력 값 1 // 0 <= 인덱스 < 1
print(dongle2.count('1', 0, 2))   # 출력 값 2 // 0 <= 인덱스 < 2

print(dongle2.count('7', 7, 8))   # 출력 값 1 // 7 <= 인덱스 < 8
print(dongle2.count('7', 7, 9))   # 출력 값 2 // 7 <= 인덱스 < 9
