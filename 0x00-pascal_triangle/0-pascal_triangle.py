#!/usr/bin/env python3
"""
0-pascal_triangle
"""
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Create a function pascal_triangle that returns a list of
    lists ofintegers representing the Pascal’s triangle of n:
    """
    outer_arr: List[List[int]] = []

    if n <= 0:  # return an empty array
        return []

    i = 1
    while i <= n:  # loop through if i < n
        inner_arr = []
        if len(outer_arr) == 0:  # if outer_arr is empty append [1]
            outer_arr.append([1])
        elif len(outer_arr) == 1:  # if len(outer_arr) is 1 append [1, 1]
            outer_arr.append([1, 1])
        else:  # Loop through last subarray in outer_arr to get next sequence
            arr = outer_arr[-1]
            inner_arr.append(1)
            for j in range(len(arr) - 1):
                inner_arr.append(arr[j] + arr[j + 1])
            inner_arr.append(1)
            outer_arr.append(inner_arr)
        i += 1
    return outer_arr
