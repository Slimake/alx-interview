#!/usr/bin/python3
"""0-validate_utf8 Module"""
from typing import Union, List


def validUTF8(data: List[int]) -> bool:
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    for value in data:
        if isinstance(value, int):
            binary = bin(value)
            if len(binary[2:]) <= 8:
                continue
            else:
                return False
        else:
            return False
    return True
