#!/usr/bin/env python
import sys

for line in open(sys.argv[1]):
    if line[0] == ">":
        for c in line:
            if c == "=":
                c = "_"
            sys.stdout.write(c)
    else:
        print(line.rstrip())
