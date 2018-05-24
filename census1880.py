#imports
import csv
from func_defs import *


def writeName1880 (c , g, config_dict):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 NameWriter(row,'3-Name','8-Relationship', the_file)

                 #Call SexWriter Function
                 SexWriter(row,'5-Sex',the_file)

                 #Call YBdateWriter function
                 YBdateWriter (row,'6-Age','1880',the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,'24-POB',the_file)

                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1880')

                 #call OccupationWriter function
                 if config_dict["Occupation"] == 1:
                    OccupationWriter(row, config_dict["occupTag"], '13-Occupation', the_file, '1880')

                 #call RaceWriter function
                 if config_dict["Race"] == 1:
                    RaceWriter(row,'4-Color', config_dict["raceTag"], the_file, '1880')

                 #call LiteracyWriter1880 function
                 if config_dict["Literacy"] == 1:
                    LiteracyWriter1880(row,'22-Cannot read','23-Cannot write', '6-Age',config_dict["literTag"], the_file, '1880')

                 #call DeafWriter1880 function
                 if config_dict["Disability"] == 1:
                    DeafWriter1880(row, '17-Deaf and Dumb',config_dict["disiTag"], the_file)

                 #call BlindWriter function
                 if config_dict["Disability"] == 1:
                    BlindWriter(row,'16-Blind', config_dict["disiTag"],the_file)

                 #call SickOrDisabledWriter function
                 if config_dict["Disability"] == 1:
                    SickOrDisabledWriter(row,'15-sick or disabled', config_dict["disiTag"],the_file )

                 #call IdioticWriter function
                 if config_dict["Disability"] == 1:
                    IdioticWriter(row, '18-Idiotic', config_dict["disiTag"],the_file)

                 #call InsaneWriter function
                 if config_dict["Disability"] == 1:
                    InsaneWriter(row, '19-Insane', config_dict["disiTag"],the_file)

                 #call MaimedWriter function
                 if config_dict["Disability"] == 1:
                    MaimedWriter(row,'20-Maimed etc.' ,config_dict["disiTag"],config_dict["propTag"],the_file)

                 #call FamilyWriter1880 function
                 FamilyWriter1880(row, '8-Relationship', '12-Married in Year.', the_file,idn, '1880')

            #call endfile function
             EndFile(the_file)
                 
