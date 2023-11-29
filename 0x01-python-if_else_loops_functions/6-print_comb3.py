#!/usr/bin/python3
for n in range(9):
    for j in range(n + 1, 10):
        if n * 10 + j < 89:
            print("{:d}{:d}".format(n, j), end=", ")
print("{:d}".format(89))
