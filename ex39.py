states ={
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}
cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print '-'*10
print "NY state has:",cities['NY']
print "OR state has:",cities['OR']
print '-'*10
print "Michigan's abbreviation is:",states['Michigan']
print "Florida's abbreviation is:",states['Florida']
print '-'*10
print "Michigan has:",cities[states['Michigan']]
print "Michigan has:",cities[states['Florida']]
print '-'*10
for state,abbrev in states.items() :
	print "%s is the abbreviation of %s" %(abbrev,state) 
print '-'*10
for abbrev,city in cities.items():
	print "%s has the %s" % (abbrev,city)
print '-'*10
