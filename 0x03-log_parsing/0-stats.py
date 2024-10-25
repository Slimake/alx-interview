#!/usr/bin/env python3
"""0-stats Module"""

import sys
import re
import signal

num = 0
status_counter = 0
status_dict = {}
file_size = 0


def signal_handler(sig, frame):
    """Call signal_handler when a SIGINT is triggered"""
    print(f"File size: {file_size}")
    for key, value in sorted(status_dict.items()):
        print(f"{key}: {value}")
    sys.exit(0)


# Set up the signal handler
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    num += 1
    prog = re.compile(
        r'^([\d\.]+) - \[([^\]]+)\] '
        r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    )
    result = prog.match(line)  # check if pattern match line

    if result is not None:
        try:
            status_code = int(line.split(' ')[-2])
            if status_code in status_dict:
                status_dict[status_code] += 1
            else:
                status_dict[status_code] = 1
        except ValueError:
            pass

        size = int(line.split(' ')[-1])
        file_size += size
        if num == 10:
            num = 0
            print(f"File size: {file_size}")
            output_dict = status_dict.copy()
            for key, value in sorted(status_dict.items()):
                print(f"{key}: {value}")
