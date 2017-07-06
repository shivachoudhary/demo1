# ! usr/bin/python
## ussage avg of two numbers ....

n_value=int(input("enter the n_value"))
t=n_value
list_=[]
while n_value:
	value=int(input())
	list_.append(value)
	n_value=n_value-1
sum=0
for i in list_:
	sum=sum+i
avg=sum/t

print "Tottal marks {} and it's average is{} ::".format(sum,avg)

