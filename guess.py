#usr/bin/python


print "Hiii Welcome to the guessme:: __/!\__"

print "Can u play the game y/n::"

a=raw_input()
import sys
if a=='n':
	print "It's Okkk __/\__"
	sys.exit()

print "Thank uu for choosing the game ::"
print "please listen the instructions before playing the game:::"
system_Input=129
c=0
while(1) :
	print "please enter the input is Integer _valueee ::: "
	user_input=input()
	c=c+1
	if user_input==system_Input : 
		print "Heyyy bugyyy u are gusssing correctly "
		print "U r guessing takes {} no of inputs ".format(c)
		break
	elif user_input>system_Input :
		print "Heyyy u r gussing veryyy larger value Better to Guess next Time::"
	elif user_input<system_Input :
		print "Heyyy U r Gussing Veryy smaller Value Better to Guess Next Time ::"

print "U r Total no of guesses is {}".format(c)
print "Thank UU for Playing the GuessMe __/\__"

