#factory function for fibonachi function
def caching_fibonacci():
    cache = {}
    #calculating fibonachi for n where n is a number
    def fibonacci(n: int):
        if type(n) is not int:
            return 0
        if n <= 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(-10))  # Виведе 0
print(fib('asd'))  # Виведе 0

