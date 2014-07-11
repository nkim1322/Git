x = "There are %d types of people." %10

binary = "binary"
do_not = "don't"

# string within a string using formatting symbols (be aware of format for multiple- need parentheses)
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x 
print "I also said :'%s'." % y 

# boolean
hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"


print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e