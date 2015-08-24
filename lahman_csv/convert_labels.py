#!/usr/bin/env python
"""
Converts Lahman style labels to django style
thisLabelID -> this_label_id

usage:
python convert_labels <label_file>
"""

import sys

def convert_line(line):
    for c in line:
        if c.isupper() and previous.islower():
            yield "_" + c.lower()
        else:
            yield c.lower()
        previous = c

def convert(file_name):
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            #convert_line(line)
            print "".join(list(convert_line(line))) + "= models.CharField(max_length=30)"
        
def main():
    usage = "usage:\n\tpython convert_labels <label_file>"
    if len(sys.argv) < 2:
        print usage
    else:
        convert(sys.argv[1])
        
if __name__ == "__main__":
    main()
        
