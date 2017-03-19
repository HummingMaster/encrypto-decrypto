size = int(input("Enter size: "))


def fibonacci(size):
    fib_ls = []
    for number in range(0, size + 1):
        fib = (((1 + 5 ** 0.5)/2) ** number - ((1 - 5 ** 0.5)/2) ** number)/5 ** 0.5
        fib_ls.append(int(fib))
    print(fib_ls)

fibonacci(size)
