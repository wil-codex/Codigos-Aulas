def fibonacci_gerador(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
 
def enesimo_fibonacci(n):
    for termo in fibonacci_gerador(n):
        ultimo = termo
    print(f"Termo {n}: {ultimo}")
 
enesimo_fibonacci(10)
 