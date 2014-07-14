# import ability to use argv
from sys import argv

# must type in $ python ex15.py filename (for argv)
script, filename = argv

# assigns desired file to variable txt
txt = open(filename)

# simple printing line
print "Here's your file %r:" % filename
# command to read contents of file
print txt.read()

# ask for filename to open again
print "Type the filename again:"
file_again = raw_input("> ")

# similar to line 8, sets variable txt_again to open
txt_again = open(file_again)

# read again
print txt_again.read()