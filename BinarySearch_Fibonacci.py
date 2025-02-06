# Binary Search Algorithm
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found


# Example for Binary Search:
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
print(f"Index of {target}: {result}")


# Recursive Fibonacci Algorithm
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Example for Recursive Fibonacci:
n = 10
print("Fibonacci Sequence (Recursive):")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
print()


# Iterative Fibonacci Algorithm
def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence


# Example for Iterative Fibonacci:
n = 10
print("Fibonacci Sequence (Iterative):")
print(fibonacci_iterative(n))
