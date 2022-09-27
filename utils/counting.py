# Some utilities for counting

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def permutations(n, k):
    return factorial(n) // factorial(n-k)

def combinations(n, k):
    return permutations(n, k) // factorial(k)