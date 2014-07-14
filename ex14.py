from sys import argv

script, user_name, noun = argv
prompt = 'Answer here:'


print "Hi %s, I'm the %s script. I heard you like %s" %(user_name, script, noun)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
Guess what, I like %r too! 
""" %(likes, lives, computer, noun)