"""
@Version: 1.0
@Project: PythonCookBook
@Author: bubblelone
@Date: 2019/2/3 9:41
@File: example.py
@License: MIT
"""

"""
问题：在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

解决方案：保留有限历史记录正是 collections.deque 大显身手的时候

"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == '__main__':
    with open('python.txt') as f:
        #fu = search(f, 'python, 5')
        #print('fef')
        for line, prevlines in search(f, 'python', 5):
        #for line, prevlines in fu:
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
        print('ert')

a = [1, 2, 4, 100, 5, 6]
b = deque(maxlen=3)
for i in a:
    b.append(i)
print(b)   #保留最后几个元素
