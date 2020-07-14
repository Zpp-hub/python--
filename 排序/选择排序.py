# -*- coding: utf-8 -*-
# 选择排序其实就是取第一个数去跟后面的数比较，然后一轮之后得到最小的数在第一个，然后开始取第二个，重复之前的比较。
# 可以先举例，五个数的时候，四轮就能排序完，内循环则为外循环加1开始

# 直接调换值
List = [2, 6, 8, 3, 1]
def choose_sort1(data):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data
data = List
print(choose_sort1(data))

# 直接调换下标
List = [2, 6, 1, 3, 5]
def choose_sort2(data):
    for i in range(len(data)-1):
        max_index = i
        for j in range(i+1, len(data)):
            if data[max_index] > data[j]:
                max_index = j
        data[i], data[max_index] = data[max_index], data[i]
    return data
data = List
print(choose_sort2(data))






