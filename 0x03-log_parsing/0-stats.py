#!/usr/bin/python3
"""0-stats.py"""

import sys
import re
from collections import defaultdict

# Regular expression to match the expected log format
log_pattern = re.compile(
    r'^([\d\.]+) - \[([^\]]+)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
)

# Initialize metrics
total_file_size = 0
status_counts = defaultdict(int)
line_count = 0


def print_metrics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)

        if match:
            status_code = int(line.split(' ')[-2])
            file_size = int(line.split(' ')[-1])

            # Update metrics
            total_file_size += file_size
            status_counts[status_code] += 1
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()

except KeyboardInterrupt:
    # Print metrics on keyboard interruption
    print_metrics()
except Exception:
    pass