# print("Solution A")
# for x in range(200, 301):
# 	print(x)

# print("Solution B")
# for y in range(200, 300, 4):
# 	print(y)

# print("Prime numbers from 1 to 100")
# for 


def solution():
	a = 10
	b = 11
	c = 12

	return a+b, a+c, b+c

def sum(a, b):
	return a+b


def main(a):
	print("main", a)







def onlyprimenumber():
	flag = 0 
	

	for x in range(293, 301):
		flag = 0	
		print x
	
		for y in range(2, x):

			if x % y == 0:
				flag += 1
				break
				
		if flag == 0:
			print(x)
				






if __name__ == "__main__":
	onlyprimenumber()




















