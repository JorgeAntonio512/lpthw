# import argv
from sys import argv

# assign script and filename variables to argv
script, filename = argv

# set txt variable equal to open filename
txt = open(filename)

# print string and print txt file text
print "Here's your file %r:" % filename
print txt.read()

# take input from user
print "Type the filename again:"
file_again = raw_input("> ")

# set txt_again variable equal to open file_again
txt_again = open(file_again)

#print txt file contents
print txt_again.read()
