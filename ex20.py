# import argv
from sys import argv

# set two variables equal to argv
script, input_file = argv

# define function print_all...file read...
def print_all(f):
    print f.read()

# define function rewind...the seek goes to beginning of file
def rewind(f):
    f.seek(0)

#define function print_a_line...print the line count, and print the contents of line
def print_a_line(line_count, f):
    print line_count, f.readline()

# open file given in argv
current_file = open(input_file)

# prints whole contents of file
print "First let's print the whole file:\n"

print_all(current_file)

# rewind goes to beginning of file
print "Now let's rewind, kind of like a tape."

rewind(current_file)

# prints three lines from file, current_line is added 1 to each time
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
