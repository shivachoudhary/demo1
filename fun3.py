# !usr/bin/python
# uuasage::: learn functions
'''

def addition(a,b,c):
	return a+b+c


#print addition(b='linux',a='rocks')
#print addition('rocks','linux')


print map(addition,range(10),range(10),range(10))
#print filter(addition,range(20),range(10))'''
def check(a):
	if a%2==0:
		return a


print map(check,range(10))
print filter(check,range(10))

'''print map(lambda a:(a**a)**a,range(10))'''
print filter(None,range(10))



