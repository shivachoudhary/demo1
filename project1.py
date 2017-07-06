# !usr/bin/python
# ussage:: For Practice 

list1=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

for value in list1:
	print value[:list1.index(value)+1].upper()+value[list1.index(value)+1:]
