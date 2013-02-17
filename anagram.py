def repeatcheck(stringtocheck):
  retval = None
	letterdict = {}
	strlen = len(stringtocheck)
	print strlen
	hasrepeatingletters = False

	for i in range(0, strlen):
		if(letterdict.has_key(stringtocheck[i])):
			print '%s already in dictionary' % stringtocheck[i]
		letterdict[stringtocheck[i]] = stringtocheck[i]
	print letterdict

def isAnagram(string1, string2):
	""" Two strings are anagrams if they have the same letters in any order. 
	They should have the same length 
	"""
	string1length = len(string1)
	string2length = len(string2)
	string2 = string2.lower()

	if(string1 == string2):
		print "These strings are the same. They are not anagrams"
	elif(string1length == string2length):
		#the string lengths are the same
		foundstring = True
		for i in range(0, string1length):
			charac = string1[i].lower()
			if(string2.find(charac) == -1):
				foundstring = False
				break

		if(foundstring):
			print 'The strings are anagrams'
		else:
			print 'The strings are not anagrams'


	else:
		print "The strings are not anagrams"



if(__name__=="__main__"):
	isAnagram('Raji', 'jira')

	
