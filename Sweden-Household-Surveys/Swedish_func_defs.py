import csv
import codecs
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
	with open (relaName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			relaList.append(line.encode('utf-8'))

	#Occupation list
	with open (occuName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			occuList.append(line.encode('utf-8'))

	#Male First Name list
	with open (malName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			malList.append(line.encode('utf-8'))

	#Female First Name list
	with open (femName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			femList.append(line.encode('utf-8'))

	#Surname list
	with open (surName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			surList.append(line.encode('utf-8'))
	#return all the lists
	return(set(relaList), set(occuList), set(malList), set(femList), set(surList))
with open ('test.txt', 'w', encoding='utf-8') as the_file:
	a,b,c,d,e = wordListSetup('./Word-Lists/Relationships.txt','./Word-Lists/Occupations.txt', './Word-Lists/Swedish-First-Names-Male.txt', './Word-Lists/Swedish-First-Names-Female.txt', './Word-Lists/Swedish-last-Names.txt')
	for item in a:
		the_file.write(item.decode('utf-8'))
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
		name = set(name)
		
