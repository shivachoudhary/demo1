# !usr/bin/python
# Ussage :: u can inherite the properties from another functions


import sys
sys.path.insert(0,'/home/pc_python')

import modules as m

def add(a,b):
	return a+b



if __name__=='__main__':
	a=m.nseries(10)
	print "We are in Main Function :::"
	b=int(raw_input("please enter the 'B's value"))
	print add(a,b)
 
