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
def wordListSetup(relaName, occuName, malName, femName, bothName, surName):

	#set up the lists
	relaList = []
	occuList = []
	malList = []
	femList = []
	bothList = []
	surList = []

	#relationship list
	with open (relaName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			relaList.append(line.encode('utf-8'))
	#Occupation list
	with open (occuName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			occuList.append(line.encode('utf-8'))

	#Male First Name list
	with open (malName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			malList.append(line.encode('utf-8'))

	#Female First Name list
	with open (femName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			femList.append(line.encode('utf-8'))

	#Both Male and Female First Name list
	with open (bothName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			bothList.append(line.encode('utf-8'))

	#Surname list
	with open (surName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			surList.append(line.encode('utf-8'))

	#return all the lists
	return(set(relaList), set(occuList), set(malList), set(femList), set(bothList), set(surList))



#-------------------------------------------------------------------#
#-------------------Name Writer (universal)-------------------------#
#-------------------------------------------------------------------#
#row = row
#n = name row
#wordLists = the word lists
#the_file = the_file
def swedNameWriter(row,n, wordLists,the_file):

	#if name row doesn't exist do nothing
	if not row[n]:
		pass
	else:
		nameList1 = []
		name = row[n]
		name = name.lower()
		name = name.split(' ')

		
		for i in name:
			nameList1.append(i.encode('utf-8'))

		nameList = set(nameList1)
		rel, occ, malFirst, femFirst, bothFirst, sur = wordLists
		
		#create a list of surnames in each name field
		with open ('TempSurnames.txt', 'a', encoding='utf-8') as the_file:


			#relationship name suffixes
			suffixes = [b'dottir',b'dotter',b'dr', b'son',b'sson',b'dtr']
			
			#names in namelist in common with the ones in document
			surnames = sur.intersection(nameList)

			#check for names ending with common swedish suffixes
			for names in nameList:
				for suffix in suffixes:
					if names.endswith(suffix) and len(names) > (len(suffix) + 1 ):
						surnames.add(names)

			#write the found relationship words to file
			for item in surnames:
				the_file.write(item.decode('utf-8') + ' ')

				#new line each time
				if len(surnames) != 0:
					the_file.write('\n')

		#create a list of occupations in each name field
		with open ('TempOccupations.txt', 'a', encoding='utf-8') as the_file2:

			#occupations in namelist in common with the ones in document
			occupations = occ.intersection(nameList)

			#write the found occupation words to file
			for item in occupations:
				the_file2.write(item.decode('utf-8') + ' ')

				#new line each time
				if len(occupations) != 0:
					the_file2.write('\n')

		#create a list of Relationships in each name field
		with open ('TempRelationships.txt', 'a', encoding='utf-8') as the_file3:

			#relationships in namelist in common with the ones in document
			relationships = rel.intersection(nameList)

			#write the found relationship words to file
			for item in relationships:
				the_file3.write(item.decode('utf-8') + ' ')

				#new line each time
				if len(relationships) != 0:
					the_file3.write('\n')

		#create a list of Male first Names in each name field
		with open ('TempMaleFirsts.txt', 'a', encoding='utf-8') as the_file4:

			#Male first names in namelist in common with the ones in document
			maleFirsts = malFirst.intersection(nameList)

			#write the found names words to file
			for item in maleFirsts:
				the_file4.write(item.decode('utf-8') + ' ')

				#new line each time
				if len(maleFirsts) != 0:
					the_file4.write('\n')

		#create a list of Female first Names in each name field
		with open ('TempFemaleFirsts.txt', 'a', encoding='utf-8') as the_file5:

			#Female first names in namelist in common with the ones in document
			femaleFirsts = femFirst.intersection(nameList)

			#write the found names to file
			for item in femaleFirsts:
				the_file5.write(item.decode('utf-8') + ' ')

				#new line each time
				if len(femaleFirsts) != 0:
					the_file5.write('\n')
		
		#create a list of Both first Names in each name field
		with open ('TempBothFirsts.txt', 'a', encoding='utf-8') as the_file6:

			#both first names in namelist in common with the ones in document
			bothFirsts = bothFirst.intersection(nameList)

			#write the found names to file
			for item in bothFirsts:
				the_file6.write(item.decode('utf-8') + ' ')

				#new line each time
				if len(bothFirsts) != 0:
					the_file6.write('\n')
		
		#print words not found in any list
		for names in nameList:
			if names not in surnames and names not in occupations and names not in maleFirsts and names not in femaleFirsts and names not in bothFirsts and names not in relationships:
				print(names)

		#---compare temp lists to actual names---#
		#Determine whether male or female based on first names
		nameTypes= []

		for names in nameList1:

			#gender value > 0 is female, <0 is male, 0 is undetermined
			genderValue = 0
			

			if names in femaleFirsts:
				nameTypes.append("FemaleFirst")
			elif names in maleFirsts:
				nameTypes.append("MaleFirst")
			elif names in occupations:
				nameTypes.append("Occupation")
			elif names in relationships:
				nameTypes.append("Relationship")
			elif names in surnames:
				nameTypes.append("Surname")
			elif names in bothFirsts:
				nameTypes.append("GenderNeutralFirst")
			else:
				nameTypes.append("Unkown")

		print(nameTypes)

		#fix most unknown values
		for n, i in enumerate(nameTypes):
			if i == "Unknown" and currentIndex != 0:
				beforeIndex = nameTypes[int(i-1)]
				afterIndex = nameTypes[int(i+1)]

				#if words before and after it are first names, make unknown values first names
				if beforeIndex == "FemaleFirst" or beforeIndex == "MaleFirst" or beforeIndex == "bothFirst":
					if afterIndex == "FemaleFirst" or afterIndex == "MaleFirst" or afterIndex == "bothFirst":
						nameTypes[n] = "bothFirst"


#-------------------------------------------------------------------#
#--------------------------------End File---------------------------#
#-------------------------------------------------------------------#
def EndFile(the_file):
    #print family records
    with open('temporaryfamilies.txt', 'r') as new_file:
        familesfinal = new_file.read()
        the_file.write(familesfinal)

    #clear temporaryfamilies.txt
    with open('temporaryfamilies.txt', 'w') as new_file:
        new_file.close

    #Print Trailer
    the_file.write('TRLR\n')