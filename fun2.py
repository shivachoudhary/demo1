# !usr/bin/python
# uusage ::: fun args

def max(*args):
	sum=0
	for value in args:
		sum=sum+value
	print "Toatal_va;lue:: ",sum


max(1,2,3,4,5,6,7,8,9,10)

def add(a,b):
	a=a+b
	print 'sum is ',a
	return 0


my_num=[1,2]
add(*my_num)
my_value={'a':1,'b':34}
add(**my_value)

def callservice(**kwargs):
	if 'name' in kwargs:
		print kwargs['name']
	if 'gender' in kwargs:
		print kwargs['gender']
	if 'age' in kwargs :
		print kwargs['age']


callservice(name='siva',gender='male',age='20')
x = 10

def my_func():
  global x
  x = x + 1
  return x
  
print my_func() # 11
print x         # 11

x = 10

def my_func():
  x = 2
  print x
 # print locals()
  
my_func()   # 2
#print globals() 
print x     # 10



