# 정렬을 위한 교환 작업
list = [4, 6, 1, 3, 5, 2]


def bubblesort(list):
    for i in range(len(list)-1):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list


print(bubblesort(list))
