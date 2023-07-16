astring = "Hello World!"
astring2 = 'Hello World!'

print("single quotes are ' '")
print(len(astring))
print(astring.index("l"))
#index is to find the letter 
#len is to count the number of characters
print(astring.count("l"))
#count is to count numbers of certain character
print(astring[3:8])
#up that is to list/ only print those
#certain characters within.
#[start:stop:step]
print(astring[6:12:3])
print(astring[0:5:1])

print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello"))
print(astring.endswith("asdlkjasdlkj"))
print(astring.endswith("World!"))

afewwords = astring.split(" ")

#Excercise
s = "Strings are awesome"
print("Length of s = %d" % len(s))

print("The first occurance of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are'%s'" % s[0:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth chracter is '%s'" % s[12])
print("The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())
if s.startswith("Str"):
	print("String starts with 'Str'. Good!")
print("Split the words of the string: %s" % s.split(" "))