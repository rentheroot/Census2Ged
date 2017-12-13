#imports
import csv
from func_defs import *

def writeName1900 (c , g):
    idn = 0
    
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 NameWriter(row,"3 NAME",'4 Relationship of each person to the head of the family.', the_file)

                 #Call SewWriter Function
                 __Sex_Writer__(row,"6 Sex",the_file)

                 #call YMBdateWriter function
                 YMBdateWriter(row,"7 Year","7 Month",the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,"13 POB",the_file)

                 
                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1900')

                 #call ImmigYearWriter function
                 ImmigYearWriter(row,"16 Year of immigration to the United States.",the_file)

                 #call OccupationWriter function
                 OccupationWriter(row, "19 Occupation", the_file, '1900')

                 #call RaceWriter function
                 RaceWriter(row,'5 Color or race', the_file, '1900')

                 #call NaturalizedWriter function
                 NaturalizedWriter(row, the_file,'18 Naturalization.', '1900' )

                 #call LiteracyWriter function
                 LiteracyWriter(row,'22 Can read','23 Can write', the_file, '1900')

                 #call ChildNoWriter function
                 ChildNoWriter(row,'11 Mother of how many children.','12 Number living.',the_file, '1900')

                 #call SpeakEnglishWriter function
                 SpeakEnglishWriter(row,'24 Can speak English', the_file, '1900')

                 #call PropertyWriter function
                 PropertyWriter(row,'25 Owned or rented', '26 Owned free or mortgaged.','27 Farm or home','28 Number of farm schedule.', the_file, '1900' )

                 #call FamilyWriter1900 function
                 FamilyWriter1900(row, '4 Relationship of each person to the head of the family.','10 Years married.', the_file,idn, '1900')
                   
             #call EndFile function
             EndFile(the_file)
        
