def fib(index):
    if index == 0:
        return index
    if index == 1:
        return index

    return fib(index - 1) + fib(index - 2)


print(fib(6))
print(fib(8))
