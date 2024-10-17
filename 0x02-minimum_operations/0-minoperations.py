#!/usr/bin/python3
"""
this code will return the min no of operations
"""


def minOperations(n):
    """function to return the min no of operations"""
    if n <= 1:
        return 0

    sum = 0
    sup = n
    for i in range(2, sup + 1):
        while (n % i == 0):
            sum += i
            n = n / i

    return sum
