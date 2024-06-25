def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input("Введите количество чисел Фибоначчи: "))
fibonacci_numbers = list(fibonacci_generator(n))
print(fibonacci_numbers)