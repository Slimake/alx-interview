#!/usr/bin/python3
"""0-minoperations Module"""


def minOperations(n):
    """
    A method that calculates the fewest number of operations
    needed to result in exactly n H characters.
    """
    operation = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operation += i
            n //= i
        if n == 1:
            break

    return operation
