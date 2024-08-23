numbers = [1, 2, 3]

# def double(a):
#     return a*2

# double = lambda a : a*2

result = map(lambda a : a*2, numbers)

print(list(result))

list_tuples = [1, 2, 3, 4]
expenses = [
    ('Dave', 20),
    ('Rob', 30)
]
sum=0
for expense in expenses:
    print(expense)
    print(expense[1])
    sum += expense[1]
    print(sum)

print(expenses[1])
print(list_tuples[1])
print(sum)