from functools import reduce
numbers = [1, 2, 3]

# def double(a):
#     return a*2
# double = lambda a : a*2

result = map(lambda a : a*2, numbers)

print(list(result))

expenses = [
    ('Dave', 20),
    ('Rob', 30)
]
# sum=0
# for expense in expenses:
#     print(expense)
#     print(expense[1])
#     sum += expense[1]
#     print(sum)
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)


