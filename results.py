# !usr/bin/python
# usage: results announcement


print "Enter user name r qualified or not:::"
name=raw_input()

list1=['kalyan','supraja','mahindra','anil','siva','ajay','haritha','keerthi','suhashini','subhashini','nariyan','manoj','santhosh','kumar','niveda','thomos','rasii']

if name in list1 :
	print 'Qualified in Exams :::'
	print "congratssss---->{}".format(name)
		
else :
	print "Better luck next Time -->{}".format(name)
	
