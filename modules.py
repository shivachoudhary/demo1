# !usr/bin/python
# Ussage :: creating modules and use as many time


def nseries(a):
	sum=0
	for value in range(1,a+1):
		sum=sum+value
	return sum


def sub(a,b):
	if(a>b):
		return a-b
	else:
		return b-a



if __name__=='__main__':
	b=int(raw_input("enter a value ::"))
	print "heyyy u r entering into the main Function:::"
	print "N Summation series sum is {}".format(nseries(b))
	a=int(raw_input("enter a value ::"))
	my_num=[b,a]
	print " diff of two numbers {}".format(sub(*my_num))
