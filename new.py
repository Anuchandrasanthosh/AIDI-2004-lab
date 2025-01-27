# Generate first 10 Fibonacci numbers
a, b = 0, 1
for _ in range(11):
    print(a, end=" ")
    a, b = b, a + b
