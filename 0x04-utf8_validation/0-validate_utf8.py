#!/usr/bin/python3
"""0-validate_utf8 Module"""


def validUTF8(data):
    count = 0

    for byte in data:
        # Check the first 3 bits to determine the type of character
        if count == 0:
            if (byte & 0b11111000) == 0b11110000:  # 4-byte character
                count = 3
            elif (byte & 0b11110000) == 0b11100000:  # 3-byte character
                count = 2
            elif (byte & 0b11100000) == 0b11000000:  # 2-byte character
                count = 1
            elif (byte & 0b10000000) == 0:  # 1-byte character
                continue  # No additional bytes expected
            else:
                return False  # Invalid start byte
        else:
            # Check if the byte is a valid continuation byte
            if (byte & 0b11000000) != 0b10000000:
                return False
            count -= 1

    return count == 0
