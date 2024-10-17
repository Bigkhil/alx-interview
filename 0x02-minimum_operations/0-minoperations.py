#!/usr/bin/python3
"""
this code will return the min no of operations
"""


def minOperations(n):
    """function to return the min no of operations"""
    if n <= 1:
        return 0

    sum = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            sum += factor
            n /= factor
        factor += 1

    return sum
