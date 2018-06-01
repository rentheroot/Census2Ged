#imports
import csv
from Swedish_func_defs import *
import os

def writeName1881_1885 (c , g):
    idn = 0

    #get current working directory path
    cwd = os.getcwd()
    cwd2 = os.path.basename(cwd)

    if cwd2 == "Sweden-Household-Surveys":
        files = ['./Word-Lists/Relationships.txt','./Word-Lists/Occupations.txt', './Word-Lists/Swedish-First-Names-Male.txt', './Word-Lists/Swedish-First-Names-Female.txt','./Word-Lists/Swedish-First-Names-Both.txt', './Word-Lists/Swedish-last-Names.txt']
    else:
        files = ['./Sweden-Household-Surveys/Word-Lists/Relationships.txt','./Sweden-Household-Surveys/Word-Lists/Occupations.txt', './Sweden-Household-Surveys/Word-Lists/Swedish-First-Names-Male.txt', './Sweden-Household-Surveys/Word-Lists/Swedish-First-Names-Female.txt','./Sweden-Household-Surveys/Word-Lists/Swedish-First-Names-Both.txt', './Sweden-Household-Surveys/Word-Lists/Swedish-last-Names.txt']

    wordLists =wordListSetup(*files)

    with open(g, 'a', encoding='utf-8') as the_file:
        with open(c, newline='',encoding='utf-8') as csvfile:
             reader = csv.DictReader(csvfile)
     
             for row in reader:
                
                #number of characters in value in the alphabet
                alphaNumber = 0
                row2 = list(row)
             	#check if whole row is empty
                for i in range(len(row2)):
                    rowName = row2[i]
                    if not row[rowName]:
                        pass
                    else:
                        for char in row[rowName]:
                            if char.isalpha():
                                alphaNumber += 1

                #if the row contains at least one letter, do the stuff
                if alphaNumber != 0:

                    #print "0 @I(unique 3 digit number)@ INDI"
                    idn += 1
                    the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')


                    #name, occupation, relationship writer
                    swedNameWriter(row,"Name", wordLists, the_file, idn, '1881', '1885', 'Marriage-Married')

                    #birth date (month, day, and year) writer
                    BDateWriter(row, 'Birth-Year', 'Birth-Month-Day', 'Birth-Place', '18', the_file)

             #call endfile function
             EndFile(the_file,g, idn)