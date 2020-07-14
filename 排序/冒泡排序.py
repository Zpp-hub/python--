# -*- coding: utf-8 -*-
# 冒泡排序是从左往右每两个都进行比较，较大的值往右走，每一轮较大的值都到右端，外层循环次数还是跟选择排序一样，但内层循环要注意是到 len(list)-i-1

List = [2, 6, 8, 3, 1]


def bubble_sort1(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


data = List
print(bubble_sort1(data))

def bubble_sort2(data):
    # 将大的移动到右端
    for i in range(len(data)):
        flag = False
        for j in range(len(data) - 1 - i):
            if (data[j] > data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
        # 若移动成功
        if flag:
            flag = False
            # 将小的移动到左端
            for j in range(len(data) - i - 2, 1, -1):
                if (data[j] < data[j - 1]):
                    data[j - 1], data[j] = data[j], data[j - 1]
                    flag = True
        # 此方法高效是因为一个循环排序号一个大的和一个小的
        if not flag:
            break
    return data

data = List
print(bubble_sort2(list))



