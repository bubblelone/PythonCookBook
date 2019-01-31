
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

