f = 2
print(f == 2)
print(f == 3)
print(f <= 3)

name = "Jon"
if name in ["Jon", "Rick"]:
	print("Your name is either Jon or Rick")

statement = False
another_statement = True
if statement is False:
	print("cool")
	
	pass
elif another_statement is True:
	print("another_statement")

	pass
else:
	print("wrong!")
	pass
x = 2 
if x == 2:
	print("x equals two!")
else:
	print("x does not equal to two.")

x = [1,2,3]
y = [1,2,3]
print( x == y) #prints out True
print(x is y) #prints out False
#'is' is to directly  equals the variable, unlike == which compares the meaning.
print(not False) #prints out true
print((not False) == (False)) #prints out false

