#! /usr/bin/env python
"""
Read a csv file and prepend an auto incrementing key field
"""

import sys

out_file = open(sys.argv[1] + "new", 'w')
index = 1
with open(sys.argv[1], 'r') as f:
    for line in f:
        out_file.write("%d,%s" % (index, line))
        index += 1
    out_file.close()
