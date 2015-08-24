#/usr/bin/env python

"""
This utility takes the year field and team foreign key field and concatinates them, then overwrites the team with the result
The results are written to a file with the same name as the original with ".new" added to the end of the filename


usage:  python convert_team_foreign.py <filename> <position1> <position2> <separator>

where:
    filename is name of a csv file to be read
    position1 is the index in the row where the
convert_team -- reads old_team.csv and replaces the first value in each row with the TeamID concatinated with the year
    ex: "BOS1984"
"""
import sys

file_names = {"appearances.csv": (1,2), "pitching.csv": (2,4), "batting.csv": (2,4), "fielding.csv": (2,4), "salary.csv": (1,2)}
file_names = {"fielding.csv": (2,4)}

def process_file(in_file, p1, p2, sep):
    with open(in_file) as infile:
        with open("%s.new" % in_file, "w") as outfile:
            for line in infile:
                line_list = line.strip().split(sep)
                print line_list
                line_list[p2] = "%s%s" % (line_list[p1], line_list[p2])
                new_line = sep.join(line_list) + '\n'
                print new_line
                outfile.write(new_line)


def main(infile, p1, p2, sep):
    print infile, p1, p2, sep
    process_file(infile, int(p1), int(p2), sep)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print "usage:  python convert_team_foreign.py <filename> <position1> <position2> <separator>"
    else:
        print sys.argv
        main(*sys.argv[1:])
