from sys import argv

#in command line, write ex20.py desire_filename
script, input_file = argv

# new function called print_all, f is the argument
def print_all(f):
# read file
	print f.read()
	
# new function with f as a file variable 	
def rewind(f):
	f.seek(0)
	
#
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

#printing line by line, progressively increasing
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)