# 선택 정렬

def select_sorting(x):

    for i in range(len(x)):

        min_index = i  # 가장 작은 원소의 index

        for j in range(i + 1, len(x)):

            if x[min_index] > x[j]:
                min_index = j

        x[i], x[min_index] = x[min_index], x[i]
        # python swap

    print(x)


test_case = [1, 3, 8, 2, 9, 4, 7, 6, 5]
select_sorting(test_case)

# 삽입 정렬

def insert_sorting(y):

    for i in range(1, len(y)):

        for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법

            if y[j] < y[j - 1]:  # 한칸씩 왼쪽으로 이동

                y[j], y[j - 1] = y[j - 1], y[j]

            else:  # 자신보다 작은 데이터를 만나면 그 위치에서 멈춤
                break

    print(y)


test_case = [1, 3, 8, 2, 9, 4, 7, 6, 5]
insert_sorting(test_case)


