import csv
familynumber = 0

#-------------------------------------------------------------------#
#----------------Word lists to python lists-------------------------#
#-------------------------------------------------------------------#
#relaName - relationship word list
#occuName = occupation word list
#malName = male first names word list
#femName = female first names word list
def wordListSetup(relaName, occuName, malName, femName, surName):

	#set up the lists
	relaList = []
	occuList = []
	malList = []
	femList = []
	surList = []

	#relationship list
	with open (relaName, 'r') as the_file:
		for line in the_file:
			relaList = relaList.append(line)

	#Occupation list
	with open (occuName, 'r') as the_file:
		for line in the_file:
			occuList = occuList.append(line)

	#Male First Name list
	with open (malName, 'r') as the_file:
		for line in the_file:
			malList = malList.append(line)

	#Female First Name list
	with open (femName, 'r') as the_file:
		for line in the_file:
			femList = femList.append(line)

	#Surname list
	with open (surName, 'r') as the_file:
		for line in the_file:
			surList = surList.append(line)
	#return all the lists
	return(set(relaList), set(occuList), set(malList), set(femList), set(surList))

#-------------------------------------------------------------------#
#-------------------Name Writer (universal)-------------------------#
#-------------------------------------------------------------------#
#row = row
#n = name row
#the_file = the_file
def swedNameWriter(row,n, the_file):

	#if name row doesn't exist do nothing
	if not row[n]:
		pass
	else:
		name = row[n]
		name = list(name)
		for i in name:
