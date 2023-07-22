#!/usr/bin/python3
"""Script reads stdin line by line and computes metrics"""
import sys
import re

pattern = r'(\d+\.\d+\.\d+\.\d+)'\
    r' - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'
count = 0
status_codes = {}
total_file_size = 0


try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if not match:
            continue
        count += 1
        ip_address = match.group(1)
        date = match.group(2)
        status_code = match.group(3)
        file_size = match.group(4)

        total_file_size += int(file_size)

        if not status_code.isnumeric():
            continue

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        if count % 10 == 0:
            zipped = zip(status_codes.keys(), status_codes.values())
            lists = list(zipped)
            lists.sort(key=lambda n: n[0])
            print(f"File size: {total_file_size}")
            for k, v in lists:
                print(f"{k}: {v}")

finally:
    zipped = zip(status_codes.keys(), status_codes.values())
    lists = list(zipped)
    lists.sort(key=lambda n: n[0])
    print(f"File size: {total_file_size}")
    for k, v in lists:
        print(f"{k}: {v}")
