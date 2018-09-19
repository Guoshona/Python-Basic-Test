ten_things = "This is a test"
print "Wait a minute,fix that"
stuff = ten_things.split(" ")
print "there are %d items" % len(stuff)
more_stuff=["55","66","77","88"]
while len(stuff) != 8 :
	next_one=more_stuff.pop()
	print "Adding",next_one
	stuff.append(next_one)
	print "there are %d items" % len(stuff)
print "pint second item in stuff:",stuff[1]
print "what's this ?",stuff[-1]
print "what?",' '.join(stuff)
print "what???",'#'.join(stuff[3:5])
print stuff
