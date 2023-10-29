def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Print the first 10 Fibonacci numbers
n = 10
fibonacci_sequence = generate_fibonacci(n)
for num in fibonacci_sequence:
    print(num)