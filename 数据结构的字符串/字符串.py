# -*- coding: utf-8 -*-
# 替换空格为%20
def replaceSpace(s):
    if not s:
        return ''
    s = s.replace(' ', '%20')
    return s
print(replaceSpace('增长 '))

# 取出字符流中第一个不重复的字符
def first_not_repeating_char(string, n):
    if not string:
        return
    dict_count = {i: string.count(i) for i in string}
    res = []
    for k, v in dict_count.items():
        if v == 1:
            res.append(k)
    return res[n]
print(first_not_repeating_char('goole', 0))

# 左旋转字符串S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”
def left_rotate_string(string, n):
    if not string:
        return
    return string[n:len(string)] + string[0:n]

print(left_rotate_string('abcXYZdef', 3))
print(left_rotate_string('ab', 3))






















