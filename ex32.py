the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#for loop through a list (certain type)
for number in the_count:
	print "This is count %d" % number
	
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# for loop through mixed list
for i in change:
	print "I got %r" % i
	
# build a list, start with an empty one
elements = []

# range function
for i in range(0,6):
	print "Adding %d to the list." %i
	# append is a function that lists understand
	elements.append(i)
	
# print elements
for i in elements:
	print "Element was: %d" % i