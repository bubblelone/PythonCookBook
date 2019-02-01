
"""
问题：如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才
能从这个可迭代对象中解压出N个元素出来？

解决方案：Python的星号表达式可以用来解决这个问题

"""

"""
书中代码是return avg(middle)，然而实际上没有avg内置函数
"""
def drop_first_last(grades):
    first, *middle, last = grades
    print(type(middle), middle)
    return sum(middle)

print(drop_first_last([12,23,55,66,33,78,99,100]))


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers, type(phone_numbers))

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

"""
无论是元组、列表赋值过来，trailing 类型都是列表
"""

line ='nobody:*:-2:-2:UnprivilegedUser:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

items = [1, 10, 7, 4, 5, 9]
head, *tail = items

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

"""
if tail:#如果tail为真，返回head+sum(tail)
return head+sum(tail)
else:#否则，返回head
return head

if/else三元表达式    Y if X else Z   如果X是真，就执行表达式Y；如果X是假，则执行表达式Z
"""
