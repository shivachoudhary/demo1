# !usr/bin/python
# ussage:: attendence



student_list=['mouni','keerthi','supraja','haritha','tejeswni','manikanta','vinay','parvathi','jhansi','chandrika']

Abscent_list=['parvathi','jhansi','chandrika','lavanya','madhu','siva']

for student in student_list:
	if student in Abscent_list:
		continue
	print "report card for {}".format(student)  

