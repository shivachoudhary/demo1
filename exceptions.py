# !usr/bin/python
# ussage:: know the knowledge
import exceptions 

try:
	a=int(raw_input())
	b=int(raw_input())
	results=a/b
except ValueError,error:
	print "please enter the numeric value  "
except ZeroDivisionError, error:
	print "please enter a non-zero value  "
else:
	print results

