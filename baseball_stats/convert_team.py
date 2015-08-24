#/usr/bin/env python

"""
convert_team -- reads old_team.csv and replaces the first value in each row with the TeamID concatinated with the year
    ex: "BOS1984"
"""

with open("old_team.csv") as infile:
    with open("team.csv", "w") as outfile:
        for line in infile:
            print line
            line_list = line.split(",")
            #print line_list
            line_list[0] = "%s%s" % (line_list[1], line_list[3])
            new_line = ",".join(line_list)
            print new_line
            outfile.write(new_line)

