# def factorial(n):
#     total = 1
#     for i in range(1, n+1):
#         total *= i
#     return total


# print(factorial(3))
# print(factorial(4))

def factorial(n):
    if n == 1:
        return n

    return n * factorial(n-1)


print(factorial(3))
print(factorial(4))
