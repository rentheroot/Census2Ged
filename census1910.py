#imports
import csv

from func_defs import *


def writeName1910 (c , g, config_dict):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 NameWriter(row,"3 NAME",'4 Relationship', the_file)

                 #Call SexWriter Function
                 sex = SexWriter(row,"5 Sex",the_file)

                 #Call YBdateWriter function
                 YBdateWriter (row,"7 Age",'1910',the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,"12 POB",the_file)
                 
                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1910')

                 #call ImmigYearWriter function
                 if config_dict["Immigration"] == 1:
                    ImmigYearWriter(row,"15 Immigration", config_dict["immigTag"],the_file)

                 #call OccupationWriter1910 function
                 if config_dict["Occupation"] == 1:
                    OccupationWriter1910(row, config_dict["occupTag"], "18 Occupation","19 Industry/busines", the_file, '1910')

                 #call RaceWriter function
                 if config_dict["Race"] == 1:
                    RaceWriter(row,'6 Color',config_dict["raceTag"], the_file, '1910')

                 #call NaturalizedWriter function
                 if config_dict["Naturalize"] == 1:
                    NaturalizedWriter(row, the_file, config_dict["natuTag"],'16 Naturalized?', '1910' )

                 #call LiteracyWriter function
                 if config_dict["Literacy"] == 1:
                    LiteracyWriter(row,'23 Read','24 Write', config_dict["literTag"], the_file, '1910')

                 #call ChildNoWriter function
                 if config_dict["Children Born"] == 1:
                    ChildNoWriter(row,'10 Children born','11 Still living',  config_dict["chilTag"], the_file, '1910')

                 #call SpeakEnglishWriter function
                 if config_dict["Language"] == 1:
                    SpeakEnglishWriter(row,'17 English', config_dict["langTag"], the_file, '1910')

                 #call ArmyWriter function
                 if config_dict["Military"] == 1:
                    ArmyWriter(row, '30 Army or Navy.', config_dict["militTag"], the_file)

                 #call BlindWriter function
                 if config_dict["Disability"] == 1:
                    BlindWriter(row, '31 Blind', config_dict["disiTag"], the_file)

                 #call DeafWriter finction
                 if config_dict["Disability"] == 1:
                    DeafWriter(row, '32 Deaf, etc.', config_dict["disiTag"], the_file)

                 #call PropertyWriter function
                 if config_dict["Property"] == 1:
                    PropertyWriter(row,'26 Owned/Rented', '27 Free/Mortgage','28 Farm/house','29 # farm', config_dict["propTag"], the_file, '1910' )

                 #call FamilyWriter1900 function
                 FamilyWriter1900(row, '4 Relationship','9 Years married.', the_file,idn, '1910',sex)

            #call EndFile function
             EndFile(the_file,g, idn)
