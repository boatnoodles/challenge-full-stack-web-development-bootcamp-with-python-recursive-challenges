# def factorial(n):
#     total = 1
#     for i in range(1, n+1):
#         total *= i
#     return total


# print(factorial(3))
# print(factorial(4))

# Assumption: user has keyed in an integer
def factorial(n):
    try:
        if n < 0:
            print("enter a positive integer please")
            return False
        if n == 0 or n == 1:
            return n
        return n * factorial(n-1)
    except TypeError:
        print("enter a positive integer please")
        return False


print(factorial(0))
print(factorial(4))
