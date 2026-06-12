def fibonacci_sequence(n):
    a = 0
    b = 1
    for i in range(n):
        x = a + b
        print(a)
        a = b
        b = x

fibonacci_sequence(15)
