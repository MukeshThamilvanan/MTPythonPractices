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

#EXCERCISE
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
 	