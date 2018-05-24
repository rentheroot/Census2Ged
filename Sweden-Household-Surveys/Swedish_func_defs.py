import csv
import codecs
import config

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
#g = the output gedcom
#idn = identification number
def swedNameWriter(row,n, wordLists,g, idn):

	#if name row doesn't exist do nothing
	if not row[n]:
		pass
	else:
		#edited name list
		nameList1 = []
		#unchanged name list
		nameList2 = []

		name = row[n]
		name2 = name.split(' ')
		for i in name2:
			nameList2.append(i.encode('utf-8'))

		name = name.lower()
		name = name.split(' ')

		
		for i in name:
			nameList1.append(i.encode('utf-8'))

		nameList = set(nameList1)
		rel, occ, malFirst, femFirst, bothFirst, sur = wordLists
		
		#create a list of surnames in each name field

		#relationship name suffixes
		suffixes = [b'dottir',b'dotter',b'dr', b'son',b'sson',b'dtr']
		
		#names in namelist in common with the ones in document
		surnames = sur.intersection(nameList)

		#check for names ending with common swedish suffixes
		for names in nameList:
			for suffix in suffixes:
				if names.endswith(suffix) and len(names) > (len(suffix) + 1 ):
					surnames.add(names)


		#occupations in namelist in common with the ones in document
		occupations = occ.intersection(nameList)
		#relationships in namelist in common with the ones in document
		relationships = rel.intersection(nameList)
		#Male first names in namelist in common with the ones in document
		maleFirsts = malFirst.intersection(nameList)
		#Female first names in namelist in common with the ones in document
		femaleFirsts = femFirst.intersection(nameList)
		#both first names in namelist in common with the ones in document
		bothFirsts = bothFirst.intersection(nameList)

		#print words not found in any list
		for names in nameList:
			if names not in surnames and names not in occupations and names not in maleFirsts and names not in femaleFirsts and names not in bothFirsts and names not in relationships:
				print(names)

		#---compare temp lists to actual names---#
		#Determine whether male or female based on first names
		nameTypes= []

		for names in nameList1:

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
				nameTypes.append("Unknown")

		print(nameTypes)

		#fix unknown first name values 
		for n, i in enumerate(nameTypes):
			if i == "Unknown" and n != 0:
				beforeIndex = nameTypes[int(i-1)]
				afterIndex = nameTypes[int(i+1)]

				#if words before and after it are first names, make unknown values first names
				if beforeIndex == "FemaleFirst" or beforeIndex == "MaleFirst" or beforeIndex == "bothFirst":
					if afterIndex == "FemaleFirst" or afterIndex == "MaleFirst" or afterIndex == "bothFirst":
						nameTypes[n] = "bothFirst"
		
             
		#-----------Name writer-----------#

		firstNames = []
		lastNames = []

		with open(g, 'a', encoding='utf-8') as the_file:
			for n, i in enumerate(nameTypes):

				#first names
				if i == "FemaleFirst" or i == "MaleFirst":
					firstNames.append(nameList2[n])
				#surnames
				if i == "Surname":
					lastNames.append(nameList2[n])

			firstNames = b' '.join(firstNames)
			lastNames = b' '.join(lastNames)

			#print "1 NAME (firstname) /(lastname)/"
			the_file.write('1 NAME ' + firstNames.decode('utf-8') + '/' + lastNames.decode('utf-8') + '/\n')
			#Print "2 GIVN (firstname)"
			the_file.write('2 GIVN ' + firstNames.decode('utf-8') + '\n')
			#Print "2 SURN (lastname)"
			the_file.write('2 SURN ' + lastNames.decode('utf-8') + '\n')

		#-------Gender Writer-------#
		genderValue = 0

		#determine gender based on name
		for i in nameTypes:
			if i == "FemaleFirst":
				genderValue += 1
			if i == "MaleFirst":
				genderValue -= 1
		
		#gender value > 0 is female, <0 is male, 0 is undefined
		if genderValue > 0:
			gender = "F"
		elif genderValue < 0:
			gender = "M"
		else:
			gender = "U"

		#write the gender to the file
		with open(g, 'a', encoding='utf-8') as the_file:
			the_file.write("1 SEX " + gender + '\n')

		#-------Occupation Writer-------#
		occupationNames = []

		with open(g, 'a', encoding='utf-8') as the_file:
			for n, i in enumerate(nameTypes):
				#occupation value
				if i == "Occupation" or i == "Relationship":
					occupationNames.append(nameList2[n])

			occupationNames = b' '.join(occupationNames)
			if len(occupationNames) != 0:
				the_file.write("1 OCCU " + occupationNames.decode('utf-8') + '\n')

		#-------Relationships writer-------#
		headOfHouseTitles = {b'far', b'pappa', b'fader', b'man', b'husfader', b'enkl.', b'enkeman', 'änkl.'.encode('utf-8'), 'änkling'.encode('utf-8'), b'eg.', b'egare', 'ägare'.encode('utf-8')}
		motherWifeTitles = {b'mamma', b'mor',b'moder', b'hustru', b'fru', b'maka', b'enka', b'enk.',b'husmoder', 'änka'.encode('utf-8'), 'änk.'.encode('utf-8'), b'd.h.', b'desshustru', b'dess hustru', b'h.'}
		childTitles = {b'barn', b'son', b'dotter', b'd.', b'dtr.', b's.'}
		illegChildTitles = {b'antenuptius', b'ante nuptius', b'a.n.', 'oä.'.encode('utf-8'), 'oäkta'.encode('utf-8')}

		#head of house
		whetherHead = headOfHouseTitles.intersection(nameList)
		#mother/wife
		whetherWife = motherWifeTitles.intersection(nameList)
		#child
		whetherChild = childTitles.intersection(nameList)
		#illegitimate
		whetherIllegitimate = illegChildTitles.intersection(nameList)

		relationshipNumbers = [len(whetherHead), len(whetherWife), len(whetherChild), len(whetherIllegitimate)]
		print(relationshipNumbers)

		number = 0
		for i in relationshipNumbers:
			if i > 0:
				number +=1

		#true/false vars
		isHead = False
		isWife = False
		isChild = False

		#if the person matches no categorys or more than one assign them as head
		if number > 1 or number == 0:
			isHead = True

		#if the person matches only the head or illegitimate category, they are head
		elif relationshipNumbers[0] > 0 or relationshipNumbers[3] > 0:
			isHead = True

		#if the person matches only the wife category, they are the wife
		elif relationshipNumbers[1] > 0:
			isWife = True

		#if the person matches only the child category, they are the child
		elif relationshipNumbers[2] > 0:
			isChild = True

		
		with open(g,'a', encoding = 'utf-8') as the_file:

			#if the person is head, make them head
			if isHead:
				config.familynumber += 1
				the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

				with open('TemporaryFamilies.txt', 'a') as new_file:
					new_file.write('0 '+ '@F' + "{0:0=3d}".format(config.familynumber) + '@ FAM\n')
					new_file.write('1 HUSB ' + '@I' + "{0:0=3d}".format(idn) + '@\n')

			#if the person is the wife, make them the wife
			if isWife:
				the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

				with open('temporaryfamilies.txt', 'a') as new_file:
					new_file.write('1 WIFE ' + '@I' + "{0:0=3d}".format(idn) + '@\n')

			#if the person is the child, make them the child
			if isChild:
				
				the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')
				with open('temporaryfamilies.txt', 'a') as new_file:
					new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')

			


#-------------------------------------------------------------------#
#--------------------------------End File---------------------------#
#-------------------------------------------------------------------#
def EndFile(the_file):
    #print family records
    with open('TemporaryFamilies.txt', 'r') as new_file:
        familesfinal = new_file.read()
        the_file.write(familesfinal)

    #clear temporaryfamilies.txt
    with open('TemporaryFamilies.txt', 'w') as new_file:
        new_file.close

    #Print Trailer
    the_file.write('TRLR\n')