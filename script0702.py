#script0702.py - Enter Python Club Members using while loop
#Written by Eugen
#Date: 01.Mai, 2017
#
######################## Define Variables ###################
names_to_enter = int(input("How many Python club member names to enter? "))
names_entered = 0
#
while names_to_enter > names_entered:	#Iterate till all names entered
	member_number = names_entered +  1
	print ()
	print("Member " + str(member_number))
	first_name = input("First Name: ")
	middle_name = input("Middle Name: ")
	last_name = input("Last Name: ")
	names_entered += 1
	print() 
	print ("Member ", member_number, "is", first_name, middle_name, last_name)
