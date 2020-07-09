# -*- coding: utf-8 -*-

# 替换空格为%20
def replaceSpace(s):
    if not s:
        return ''
    s = s.replace(' ', '%20')
    return s
print(replaceSpace('增长 '))

# 取出字符流中第一个不重复的字符
# 'google'
#
# def first_not_repeating_char(string):
#     if not string:
#         return
#     temp = dict([(x, 0) for x in range(26)])
#     for s in string:
#         # ord('a') == 97
#         temp[ord(s) - 97] += 1
#     for s in string:
#         if temp[ord(s) - 97] == 1:
#             res = s
#             break
#     return res

def first_not_repeating_char(string):
    if not string:
        return
    temp = dict([(x, 0) for x in range(26)])
    for s in string:
        # ord('a') == 97
        temp[ord(s) - 97] += 1
    for s in string:
        if temp[ord(s) - 97] == 1:
            res = s
            break
    return res

first_not_repeating_char('goole')

a = 1












