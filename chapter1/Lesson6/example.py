
"""
问题：实现一个键对应多个值的字典？

解决方案：一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要
将这多个值放到另外的容器中， 比如列表或者集合里面。

"""
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(type(d))
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(type(d))
print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(type(d))
print(d)

