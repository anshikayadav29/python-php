def fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive call

# Test
num = 7
print(f"Fibonacci sequence up to {num} terms:")
for i in range(num):
    print(fibonacci(i), end=" ")
