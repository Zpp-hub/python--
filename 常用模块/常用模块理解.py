# -*- coding: utf-8 -*-
import collections
import hashlib
import requests
import psutil
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

Point = collections.namedtuple('Point', ['x', 'y'])
print(Point)
p = Point(1, 2)
print(p.x)
print(p.y)

q = collections.deque(['a', 'b', 'c'])
print(q)
# 添加
q.append('x')
q.appendleft('y')
print(q)
# 删除
q.pop()
print(q)
q.popleft()
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = collections.defaultdict(lambda: 'N/A')
print(dd)
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# 如果要保持Key的顺序，可以用OrderedDict：
od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# 统计出现的次数
c = collections.Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)


# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 要通过GET访问一个页面，只需要几行代码
r = requests.get('https://www.baidu.com/')
print(r.status_code)
print(r.text)
# 带参数的URL
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.content)
print(r.cookies)

# post传输数据
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# json
url = 'https://accounts.douban.com/login'
params = {'key': 'value'}
r = requests.post(url, json=params)

# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)










































