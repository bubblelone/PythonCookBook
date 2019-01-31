"""
@Version: 1.0
@Project: PythonCookBook
@Author: bubblelone
@Date: 2019/1/30 13:37
@File: example.py
@License: MIT
"""

"""
问题：现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变
量？
"""

"""
解决方案：任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。 唯
一的前提就是变量的数量必须跟序列元素的数量是一样的
"""

p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

name, shares, price, (year, mon, day) = data

p = (4, 5)
x, y, z = p

s = 'Hello'
a, b, c, d, e = s

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data



"""
复杂问题转换为简单问题

正则表达式中任何一个字符，都有一种规则
提取html中酒店名称， 两端固定内容，提取中间的酒店名称，
.*?aa  .*?  这两种的不同结果，机制是怎么样的， 贪婪、非贪婪
a = re.findall('a.*c', 'abcabbcccabbbbccc')  .*c结尾，贪婪，匹配字符，一路匹配过去，直到遇到最后一个c，结果为['abcabbcccabbbbccc']

a = re.findall('a.*?c', 'abcabbcccabbbbccc') .*?c结尾 ，非贪婪，匹配字符，一旦遇到c，就结束字符匹配，然后继续用改表达式往后匹配
，结果为['abc', 'abbc', 'abbbbc']


a = re.findall('ab*', 'abbbbbbbccc')   b*结尾，贪婪，匹配所有b，结果为 abbbbbbb
a = re.findall('ab*?', 'abbbbbbbccc')   b*?结尾，非贪婪，不匹配，最终结果为a

a = re.findall('^abc', 'abcabbcccabbbbccc')  以abc开头的字符,结果为abc
a = re.findall('abc$', 'abcabbcccabbbbabc')  以abc结尾的字符,结果为abc






"""