#MI LOGIC ON FACTORAL B4 TEACHERS KNOWLEDGE
#5!

# def factorial(x):
#     while x > 1:
#         y = x*x-1
#         x -=1
#     return y
# print(factorial(3))

#WRONG

def factorial(n):
    breakpoint()
    if n <= 1: return 1
    breakpoint()
    return n*factorial(n-1)
    


print(factorial(5))