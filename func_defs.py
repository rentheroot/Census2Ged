import csv
import config
import logging


logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
logging.info('Imported func_defs.py')

#-------------------------------------------------------------------#
#-------------------Birth Place Writer (Universal)------------------#
#-------------------------------------------------------------------#
#row = row
#b = POB column
#the_file = the_file
def BPlaceWriter(row,b, the_file,idn):
    if not row [b]:
        logging.info("Birthplace nonexistant for individual on line: " + str(idn + 1))

    else:
        try:

            birthplace = row[b]
            full = '2 PLAC ' + birthplace + '\n'

            #write to file and log
            the_file.write(full)

        except:

            logging.info("Could Not Recognize Birthplace: " + row[b] + " for person on line: " + str(idn + 1))

#-------------------------------------------------------------------#
#----------------Birth Year and Month Writer------------------------#
#-------------------------------------------------------------------#
#y = birth year column
#m = birth month column
def YMBdateWriter (row,y,m,the_file,idn):


    #birthdate
    if not row[y]:
        if not row [m]:
            logging.info("Birthdate information nonexistant for individual on line: " + str(idn + 1))

        else:
            try:
                month = row[m]
                month = month[:3]
                month = month.upper()
                fulldate = str(month)
                #print birth information
                the_file.write("1 BIRT" + '\n')
                full = '2 DATE ABT ' + str(fulldate) + '\n'
                the_file.write(full)
            except:
                logging.info("Could Not Recognize Birthdate: " + row[y] + ' ' + row[m] + " for person on line: " + str(idn + 1))

    else:
        year = row[y]


        if isinstance( year, int ):

            if not row[m]:
                try:
                    fulldate = str(year)
                    #print birth information
                    the_file.write("1 BIRT" + '\n')
                    full = '2 DATE ABT ' + str(fulldate) + '\n'
                    the_file.write(full)
                except:
                    logging.info("Could Not Recognize Birthdate: " + row[y] + ' ' + row[m] + " for person on line: " + str(idn + 1))

            else:
                try:
                    month = row[m]
                    month = month[:3]
                    month = month.upper()

                    fulldate = (str(month) +' ' + str(year))
                    #print birth information
                    the_file.write("1 BIRT" + '\n')
                    the_file.write('2 DATE ABT ' + str(fulldate) + '\n')
                except:
                    logging.info("Could Not Recognize Birthdate: " + row[y] + ' ' + row[m] + " for person on line: " + str(idn + 1))
        else:
            try:  
                #print birth information
                the_file.write("1 BIRT" + '\n')
                the_file.write('2 DATE ABT ' + str(year) + '\n')
            except:
                logging.info("Could Not Recognize Birthdate: " + row[y] + ' ' + row[m] + " for person on line: " + str(idn + 1))

#-------------------------------------------------------------------#
#-----------------Birth Year Writer (Requires Age)------------------#
#-------------------------------------------------------------------#
#a = age column
#y = census year
def YBdateWriter (row,a,y,the_file):
    #print birth information
    the_file.write("1 BIRT" + '\n')

    #birthdate
    if not row[a]:
        pass

    else:
        age = row[a]

        try:
            year = int(y) - int(age)

            fulldate = str(year)
            the_file.write('2 DATE ABT ' + str(fulldate) + '\n')
        except:

            the_file.write('2 DATE ABT ' + str(y) + '\n')
#-------------------------------------------------------------------#
#----------------Name Writer (No relationship required)-------------#
#-------------------------------------------------------------------#
#n = the Name column row
#row = row
#the_file = the_file
def __Name_Writer_No_Relation__(row, n, the_file,idn):
    #separate values for firstname and lastname
    name = str(row[n]).split()
    try:
        #set last name to first word in full name
        lastname = name[0]

        #delete the lastname from the full name
        del name[0]

        firstname = (' ').join(name)


        #print "1 NAME (firstname) /(lastname)/"
        the_file.write('1 NAME ' + firstname + '/' + lastname + '/\n')
        #Print "2 GIVN (firstname)"
        the_file.write('2 GIVN ' + firstname + '\n')
        #Print "2 SURN (lastname)"
        the_file.write('2 SURN ' + lastname + '\n')
    except:
        logging.info("Could Not Recognize Name: " + row[n] + " for person on line: " + str(idn + 1))


#-------------------------------------------------------------------#
#-------------------Name Writer (Requires Relationship)-------------#
#-------------------------------------------------------------------#
#n = the Name column row
#r = relationship row
#row = row
#the_file = the_file
def NameWriter(row, n, r, the_file, idn):
    #separate values for firstname and lastname
    name = str(row[n]).split()

    try:
        relation = row[r].lower()

        #if they are the wife of the head
        if relation == 'wife' or relation == 'mother':
            #set last name to first word in full name
            lastname = name[0]

            #delete the lastname from the full name
            del name[0]

            firstname = (' ').join(name)

            #print "1 NAME (firstname) //"
            the_file.write('1 NAME ' + firstname + '//\n')

            #Print "2 GIVN (firstname)"
            the_file.write('2 GIVN ' + firstname + '\n')

        else:

            #set last name to first word in full name
            lastname = name[0]

            #delete the lastname from the full name
            del name[0]

            firstname = (' ').join(name)

            #print "1 NAME (firstname) /(lastname)/"
            the_file.write('1 NAME ' + firstname + '/' + lastname + '/\n')
            #Print "2 GIVN (firstname)"
            the_file.write('2 GIVN ' + firstname + '\n')
            #Print "2 SURN (lastname)"
            the_file.write('2 SURN ' + lastname + '\n')
    except:
        logging.info("Could Not Recognize Name: " + row[n] + " for person on line: " + str(idn + 1))

#-------------------------------------------------------------------#
#---------------------------Sex Writer------------------------------#
#-------------------------------------------------------------------#
#s is the sex column
def SexWriter(row,s, the_file,idn):
    #Print Sex
    if not row[s]:
        the_file.write("1 SEX U" + '\n')
        logging.info("Could not recognize sex of person on line: " + str(idn+1))
    else:
        sex = row[s]
        sex = sex[:1].upper()
        the_file.write("1 SEX " + sex + '\n')
        return(sex)

#-------------------------------------------------------------------#
#--------------------Immigration Year Writer------------------------#
#-------------------------------------------------------------------#
#row =row
#I = Immigration Year column
#the_file = the_file
#immigTag = Immigration tag to use
def ImmigYearWriter(row, I, immigTag, the_file):
    if not row[I]:
        pass

    else:
        if immigTag == "IMMI":
            immigyear = row[I]
            the_file.write("1 IMMI\n")
            the_file.write("2 DATE ABT " + immigyear + '\n')
        else:
            immigyear = row[I]
            the_file.write("1 EVEN\n")
            the_file.write("2 TYPE " + immigTag + '\n')
            the_file.write("2 DATE ABT " + immigyear + '\n')




#-------------------------------------------------------------------#
#-------------------------Census Year Writer------------------------#
#-------------------------------------------------------------------#
#the_file = the_file
#y = census year
def CensusYearWriter(the_file, y):
    the_file.write("1 CENS\n")
    the_file.write("2 DATE " + y +"\n")

#-------------------------------------------------------------------#
#--------------------------Occupation Writer------------------------#
#-------------------------------------------------------------------#
#row=row
#o=occupation
#the_file = the_file
#y = census year
#occuTag = occupation tag to use
def OccupationWriter(row, occuTag,o, the_file, y):
    if not row[o]:
        pass

    else:
        if occuTag == "OCCU":
            occupation = row[o]
            the_file.write("1 OCCU " + occupation + '\n')
            the_file.write("2 DATE " + y +"\n")

        #if user has selected a custom tag, use it
        else:
            occupation = row[o]
            the_file.write("1 EVEN " + occupation + '\n')
            the_file.write("2 TYPE " + occuTag + '\n')
            the_file.write("2 DATE " + y + '\n')


#-------------------------------------------------------------------#
#--------------------------Occupation Writer 1910-------------------#
#-------------------------------------------------------------------#
#row=row
#o=occupation
#the_file = the_file
#y = census year
#occuTag = occupation tag to use
def OccupationWriter1910(row, occuTag, o, I, the_file, y):
    if not row[o]:
        pass

    else:
        if occuTag == "OCCU":

            occupation = row[o]
            industry = row[I]
            the_file.write("1 OCCU " + 'Occupation: '+occupation + ' Industry: '+ industry+'\n')
            the_file.write("2 DATE " + y +"\n")

        #if user has selected a custom tag, use it
        else:
            occupation = row[o]
            industry = row[I]
            the_file.write("1 EVEN " + 'Occupation: '+occupation + ' Industry: '+ industry+'\n' )
            the_file.write("2 TYPE " + occuTag + '\n')
            the_file.write("2 DATE " + y + '\n')

#-------------------------------------------------------------------#
#-----------------------------Race Writer---------------------------#
#-------------------------------------------------------------------#
#row=row
#r = race column
#the_file=the_file
#y = census year
#raceTag = race tag to use
def RaceWriter(row, r, raceTag, the_file, y):
    race = row[r]
    if not row[r]:
        pass

    else:

        if raceTag == "DSCR":
            the_file.write('1 DSCR Race: ' + race + '\n')
            the_file.write('2 DATE ' + y +'\n')

        #if user has selected a custom tag, use it
        else:

            the_file.write("1 EVEN " + race +'\n' )
            the_file.write("2 TYPE " + raceTag + '\n')
            the_file.write("2 DATE " + y + '\n')


#-------------------------------------------------------------------#
#-------------------Naturalization Status Writer--------------------#
#-------------------------------------------------------------------#
#row=row
#the_file=the_file
#n=naturalization column
#natuTag = Naturalization tag to use
def NaturalizedWriter (row, the_file, natuTag,n, y):
    naturalized = row[n]

    if not row[n]:
        pass
    else:
        if natuTag == "NATU":
            the_file.write('1 NATU Naturalization Status: ' + naturalized +'\n')
            the_file.write('2 DATE ' + y +'\n')

        #if user has selected a custom tag, use it
        else:
            the_file.write("1 EVEN " + naturalized +'\n' )
            the_file.write("2 TYPE " + natuTag + '\n')
            the_file.write("2 DATE " + y + '\n')

#-------------------------------------------------------------------#
#---------------------------Literacy Writer-------------------------#
#-------------------------------------------------------------------#
#row=row
#r=read column
#w=write column
#the_file=the_file
#y = census year
#literTag = Literacy tag to use
def LiteracyWriter (row, r,w,literTag, the_file, y ):
    canread = row[r]
    canwrite = row[w]
    if not row[r]:
        pass
    else:
        if literTag == "EDUC":

            the_file.write('1 DSCR Can Read: ' + canread + ' Can Write: ' + canwrite + '\n')
            the_file.write('2 DATE '+ y +'\n')

        #if user has selected a custom tag, use it
        else:
            the_file.write("1 EVEN Can Read: " + canread + ' Can Write: ' + canwrite + '\n' )
            the_file.write("2 TYPE " + literTag + '\n')
            the_file.write("2 DATE " + y + '\n')


#-------------------------------------------------------------------#
#----------------------Literacy Writer 1880-------------------------#
#-------------------------------------------------------------------#
#row=row
#r=read column
#w=write column
#a = age column
#the_file=the_file
#y = census year
def LiteracyWriter1880 (row, r,w, a, the_file, y ):
    canread = row[r]
    canwrite = row[w]
    age = row[a]

    #if they can read
    if not row[r]:

        #if they can write
        if not row[w]:

            #if age column empty
            if not row[a]:
                pass
            #if age column not empty
            else:

                #check if age is under 10
                try:
                    if age < int(10):
                        pass
                    else:
                        the_file.write('1 DSCR Can Read: yes' + ' Can Write: yes' + '\n')
                        the_file.write('2 DATE '+ y +'\n')
                except:
                    pass
        #if they cannot write
        else:
            try:
                if age < int(10):
                    pass
                else:
                    the_file.write('1 DSCR Can Read: yes' + ' Can Write: no' + '\n')
                    the_file.write('2 DATE '+ y +'\n')
            except:
                pass
    #if they cannot read
    else:
        #if they can write
        if not row[w]:
            try:
                if age < int(10):
                    pass
                else:
                    the_file.write('1 DSCR Can Read: no' + ' Can Write: yes' + '\n')
                    the_file.write('2 DATE '+ y +'\n')
            except:
                pass
        #if they cannot write
        else:
            try:
                if age < int(10):
                    pass
                else:
                    the_file.write('1 DSCR Can Read: no' + ' Can Write: no' + '\n')
                    the_file.write('2 DATE '+ y +'\n')
            except:
                pass

#-------------------------------------------------------------------#
#----------------------Literacy Writer 1860-------------------------#
#-------------------------------------------------------------------#
#row=row
#r=read and write column
#a = age column
#the_file=the_file
#y = census year
def __Literacy_Writer_1860__ (row, r, a, the_file, y ):
    canread = row[r]
    age = row[a]

    #if they can read
    if not row[r]:

        #if age column empty
        if not row[a]:
            pass
        #if age column not empty
        else:

            #check if age is under 20
            try:
                if age < int(20):
                    pass
                else:
                    the_file.write('1 DSCR Can Read and write: yes' + '\n')
                    the_file.write('2 DATE '+ y +'\n')
            except:
                pass
    #if they cannot read
    else:
        try:
            if age < int(20):
                pass
            else:
                the_file.write('1 DSCR Can Read and write: no'+ '\n')
                the_file.write('2 DATE '+ y +'\n')
        except:
            pass
#-------------------------------------------------------------------#
#------------------------Child Number Writer------------------------#
#-------------------------------------------------------------------#
#row=row
#n= Number Children column
#l= Living Children column
#the_file=the_file
#y=census year
#chilTag = Children Born Tag to use
def ChildNoWriter (row, n,l, chilTag, the_file,y):
    if not row[n]:
        pass
    else:
        if chilTag == "DSCR":
            childrenborn = row[n]
            livingchildren = row[l]
            the_file.write('1 DSCR Mother of how many children: ' + childrenborn + ' Number of living children: ' + livingchildren + '\n')
            the_file.write('2 DATE '+y +'\n')

        #if user has selected a custom tag, use it
        else:
            childrenborn = row[n]
            livingchildren = row[l]
            the_file.write('1 EVEN Mother of how many children: ' + childrenborn + ' Number of living children: ' + livingchildren + '\n')
            the_file.write("2 TYPE " + chilTag + '\n')
            the_file.write("2 DATE " + y + '\n')


#-------------------------------------------------------------------#
#------------------------English Ability Writer---------------------#
#-------------------------------------------------------------------#
#row=row
#e=Speaks English? row
#the_file=the_file
#y= census year
#langTag = language spoken Tag to use

def SpeakEnglishWriter (row, e, langTag, the_file,y):
    speaksenglish = row[e]
    if not row[e]:
        pass

    else:
        if langTag == "DSCR":
            the_file.write('1 DSCR Able to speak English: ' + speaksenglish + '\n')
            the_file.write('2 DATE ' + y + '\n')

        #if user has selected a custom tag, use it
        else:
            the_file.write('1 EVEN Able to speak English: ' + speaksenglish + '\n')
            the_file.write("2 TYPE " + langTag + '\n')
            the_file.write("2 DATE " + y + '\n')

#-------------------------------------------------------------------#
#-----------------------------Property Writer-----------------------#
#-------------------------------------------------------------------#
#row=row
#o= Own or Rent column
#fm = owned free or mortgaged column
#fh = farm or home column
#fs = No. of Farm Schedule column
#the_file = the_file
#y= Census Year
#propTag = tag to use for the property information
def PropertyWriter(row, o , fm , fh , fs , propTag, the_file , y):
    ownorrent = row[o]
    freeormort = row[fm]
    farmorhome = row[fh]
    farmschedule = row [fs]

    if not row[o]:
        pass
    else:
        if propTag == "PROP":
            the_file.write('1 PROP House owned or rented: ' + ownorrent + ' Owned free or mortgaged: ' + freeormort + ' Farm or house: ' + farmorhome + ' Number of Farm Schedule: ' + farmschedule + '\n')
            the_file.write('2 DATE '+ y +'\n')
        else:
            the_file.write('1 EVEN House owned or rented: ' + ownorrent + ' Owned free or mortgaged: ' + freeormort + ' Farm or house: ' + farmorhome + ' Number of Farm Schedule: ' + farmschedule + '\n')
            the_file.write("2 TYPE " + propTag + '\n')
            the_file.write("2 DATE " + y + '\n')

#-------------------------------------------------------------------#
#------------------------Property Writer 1860-----------------------#
#-------------------------------------------------------------------#
#row=row
#r= Real estate value column
#p =personal estate column
#the_file = the_file
#y= Census Year
#propTag = tag to use for the property information
def __Property_Writer_1860__(row, r, p, the_file , propTag, y):
    realEstate = row[r]
    personalEstate = row[p]

    #doesn't have real estate
    if not row[r]:
        #doesn't have personal estate
        if not row [p]:
            pass
        #has personal estate
        else:
            if propTag == "PROP":
                the_file.write('1 PROP Value of Personal Estate: ' + personalEstate + '\n')
                the_file.write('2 DATE '+ y +'\n')
            else:
                the_file.write('1 EVEN Value of Personal Estate: ' + personalEstate + '\n')
                the_file.write("2 TYPE " + propTag + '\n')
                the_file.write("2 DATE " + y + '\n')

    #has real estate
    else:
        #doesn't have personal estate
        if not row [p]:
            if propTag == "PROP":

                the_file.write('1 PROP Value of Real Estate: ' + realEstate + '\n')
                the_file.write('2 DATE '+ y +'\n')
            else:
                the_file.write('1 EVEN Value of Real Estate: ' + realEstate + '\n')
                the_file.write("2 TYPE " + propTag + '\n')
                the_file.write("2 DATE " + y + '\n')
        #has personal estate
        else:
            if propTag == "PROP":
                the_file.write('1 PROP Value of Real Estate: ' + realEstate + 'Value of Personal estate: ' + personalEstate + '\n')
                the_file.write('2 DATE '+ y +'\n')
            else:
                the_file.write('1 EVEN Value of Real Estate: ' + realEstate + 'Value of Personal estate: ' + personalEstate + '\n')
                the_file.write("2 TYPE " + propTag + '\n')
                the_file.write("2 DATE " + y + '\n')

#-------------------------------------------------------------------#
#------------------------Property Writer 1850-----------------------#
#-------------------------------------------------------------------#
#row=row
#r= Real estate value column
#the_file = the_file
#y= Census Year
#propTag = tag to use for the property information
def __Property_Writer_1850__(row, r, the_file , propTag, y):
    realEstate = row[r]
    if not row[r]:
        pass
    else:
        if propTag == "PROP":
            the_file.write('1 PROP Value of Real Estate: ' + realEstate + '\n')
            the_file.write('2 DATE '+ y +'\n')

        else:
            the_file.write('1 EVEN Value of Real Estate: ' + realEstate + '\n')
            the_file.write("2 TYPE " + propTag + '\n')
            the_file.write("2 DATE " + y + '\n')
#-------------------------------------------------------------------#
#---------------------------Family Writer 1900 format---------------#
#-------------------------------------------------------------------#
#row=row
#r = relationship to head column
#familynumber=familynumber
#ym = years married
#the_file = the_file
#idn=idn
#y = census year
def FamilyWriter1900(row, r,ym, the_file, idn,y,sex):
    if not row[r]:
        relation = 'head'

    else:
        relation = row[r]
        relation = relation.lower()

    if relation == 'head':
        config.familynumber += 1
        the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

        with open('temporaryfamilies.txt', 'a') as new_file:
            new_file.write('0 '+ '@F' + "{0:0=3d}".format(config.familynumber) + '@ FAM\n')
            if sex.lower() == 'm':
                new_file.write('1 HUSB ' + '@I' + "{0:0=3d}".format(idn) + '@\n')
            else:
                new_file.write('1 WIFE ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


    elif relation != 'head':
        if relation == 'wife':
            yrsmarried = row[ym]
            marriageyear = int(yrsmarried)
            marriageyear = int(y) - marriageyear

            the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')


            with open('temporaryfamilies.txt', 'a') as new_file:
                new_file.write('1 WIFE ' + '@I' + "{0:0=3d}".format(idn) + '@\n')
                new_file.write('1 MARR\n')
                new_file.write('2 DATE ABT ' + str(marriageyear) + '\n')

        elif relation == 'son':

            the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

            with open('temporaryfamilies.txt', 'a') as new_file:
                new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


        elif relation == 'daughter':

            the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

            with open('temporaryfamilies.txt', 'a') as new_file:
                new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


        elif relation == 'child':

            the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

            with open('temporaryfamilies.txt', 'a') as new_file:
                new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


        else:
            print('Other Relation')


    else:
        print("im lost")

    return(config.familynumber)
#-------------------------------------------------------------------#
#---------------------------Family Writer 1880 format---------------#
#-------------------------------------------------------------------#
#row=row
#r = relationship to head column
#familynumber=familynumber
#ym = Married in year
#the_file = the_file
#idn=idn
#y = census year
def FamilyWriter1880(row, r,ym, the_file, idn,y):
    if not row[r]:
        relation = 'head'

    else:
        relation = row[r]
        relation = relation.lower()

    if relation == 'head':
        config.familynumber += 1
        the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')



        with open('temporaryfamilies.txt', 'a') as new_file:
            new_file.write('0 '+ '@F' + "{0:0=3d}".format(config.familynumber) + '@ FAM\n')
            new_file.write('1 HUSB ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


    elif relation != 'head':
        if relation == 'wife':
            if not row[ym]:
                the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')
                with open('temporaryfamilies.txt', 'a') as new_file:
                    new_file.write('1 WIFE ' + '@I' + "{0:0=3d}".format(idn) + '@\n')
                    new_file.write('1 MARR\n')

            else:
                the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

                marriageyear = y


                with open('temporaryfamilies.txt', 'a') as new_file:
                    new_file.write('1 WIFE ' + '@I' + "{0:0=3d}".format(idn) + '@\n')
                    new_file.write('1 MARR\n')
                    new_file.write('2 DATE ABT ' + str(marriageyear) + '\n')
        elif relation == 'son':

            the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

            with open('temporaryfamilies.txt', 'a') as new_file:
                new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')



        elif relation == 'daughter':

            the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

            with open('temporaryfamilies.txt', 'a') as new_file:
                new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


        elif relation == 'child':

            the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

            with open('temporaryfamilies.txt', 'a') as new_file:
                new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


        else:
            print('Other Relation')


    else:
        print("im lost")

    return(config.familynumber)
#-------------------------------------------------------------------#
#---------------------------Army/Navy Writer------------------------#
#-------------------------------------------------------------------#
#row=row
#a= Army or Navy column
#the_file=the_file
#militTag = tag to use for military service information

def ArmyWriter(row, a, militTag, the_file):
    if not row[a]:
        pass
    else:

        if militTag == "DSCR":
            militarystatus = row[a]
            the_file.write('1 DSCR Army or Navy: ' + militarystatus + '\n')
        else:
            militarystatus = row[a]
            the_file.write('1 EVEN Army or Navy: ' + militarystatus + '\n')
            the_file.write("2 TYPE " + militTag + '\n')


#-------------------------------------------------------------------#
#------------------------------Blind Writer-------------------------#
#-------------------------------------------------------------------#
#row=row
#b=Blind cloumn
#the-file=the_file
#disiTag = tag to use for disability
def BlindWriter(row, b, disiTag, the_file):
    if not row[b]:
        pass
    else:
        if disiTag == "DSCR":
            blindness = row[b]
            the_file.write('1 DSCR Whether Blind: ' + blindness + '\n')
        else:
            blindness = row[b]
            the_file.write('1 EVEN Whether Blind: ' + blindness + '\n')
            the_file.write("2 TYPE " + disiTag + '\n')



#-------------------------------------------------------------------#
#------------------------------Deaf Writer--------------------------#
#-------------------------------------------------------------------#
#row=row
#d=Deaf cloumn
#the-file=the_file
#disiTag = tag to use for disability
def DeafWriter(row, d, disiTag, the_file):
    if not row[d]:
        pass
    else:
        if disiTag == "DSCR":
            deafness = row[d]
            the_file.write('1 DSCR Whether Deaf: ' + deafness + '\n')
        else:
            deafness = row[d]
            the_file.write('1 EVEN Whether Deaf: ' + deafness + '\n')
            the_file.write("2 TYPE " + disiTag + '\n')


#-------------------------------------------------------------------#
#-------------------------Deaf Writer 1880--------------------------#
#-------------------------------------------------------------------#
#row=row
#d=Deaf cloumn
#the-file=the_file
#disiTag = tag to use for disabilty writer
def DeafWriter1880(row, d,disiTag, the_file):
    if not row[d]:
        pass
    else:
        if disiTag == "DSCR":
            deafness = row[d]
            the_file.write('1 DSCR Whether Deaf and Dumb: ' + deafness + '\n')

        else:
            deafness = row[d]
            the_file.write('1 EVEN Whether Deaf: ' + deafness + '\n')
            the_file.write("2 TYPE " + disiTag + '\n')

#-------------------------------------------------------------------#
#----------------------Sick or Disabled Writer----------------------#
#-------------------------------------------------------------------#
#row=row
#s=Sick or disabled column
#the-file=the_file
#disiTag = tag to use for disabilty writer
def SickOrDisabledWriter(row, s,disiTag, the_file):
    if not row[s]:
        pass
    else:
        if disiTag == "DSCR":

            sick = row[s]
            the_file.write('1 DSCR Whether Sick or Disabled: ' + sick + '\n')


        else:
            sick = row[s]
            the_file.write("1 EVEN Whether Sick or Disabled: " + sick + '\n')
            the_file.write("2 TYPE " + sick + '\n')


#-------------------------------------------------------------------#
#---------------------------Idiotic Writer--------------------------#
#-------------------------------------------------------------------#
#row=row
#d= Idiotic column
#the-file=the_file
#disiTag = tag to use for disabilty writer
def IdioticWriter(row, d, disiTag, the_file):
    if not row[d]:
        pass
    else:
        if disiTag == "DSCR":
            idiot = row[d]
            the_file.write('1 DSCR Whether Idiotic: ' + idiot + '\n')

        else:
            idiot = row[d]
            the_file.write("1 EVEN Whether Idiotic: " + idiot + '\n')
            the_file.write("2 TYPE " + idiot + '\n')

#-------------------------------------------------------------------#
#---------------------------Insane Writer---------------------------#
#-------------------------------------------------------------------#
#row=row
#n= Insane column
#the-file=the_file
#disiTag = tag to use for disabilty writer
def InsaneWriter(row, n, disiTag, the_file):
    if not row[n]:
        pass
    else:
        if disiTag == "DSCR":
            insane = row[n]
            the_file.write('1 DSCR Whether Insane: ' + insane + '\n')
        else:
            insane = row[n]
            the_file.write("1 EVEN Whether Insane: " + insane + '\n')
            the_file.write("2 TYPE " + insane + '\n')

#-------------------------------------------------------------------#
#---------------------------Maimed Writer---------------------------#
#-------------------------------------------------------------------#
#row=row
#m= Maimed column
#the_file=the_file
#disiTag = tag to use for disabilty writer
def MaimedWriter(row, m, disiTag, the_file):
    if not row[m]:
        pass
    else:
        if disiTag == "DSCR":
            maimed = row[m]
            the_file.write('1 DSCR Whether Maimed: ' + maimed + '\n')
        else:
            maimed = row[m]
            the_file.write("1 EVEN Whether Maimed: " + maimed + '\n')
            the_file.write("2 TYPE " + maimed + '\n')


#-------------------------------------------------------------------#
#---------------------Disabled Writer 1870--------------------------#
#-------------------------------------------------------------------#
#row=row
#d=disabled cloumn
#the_file=the_file
#disiTag = tag to use for disabilty writer
def __Disabled_Writer_1870__(row, d, disiTag, the_file):
    if not row[d]:
        pass
    else:
        if disiTag == "DSCR":
            disability = row[d]
            the_file.write('1 DSCR Disability: ' + disability + '\n')
        else:
            disability = row[d]
            the_file.write("1 EVEN Disability: " + disability + '\n')
            the_file.write("2 TYPE " + disability + '\n')

#-------------------------------------------------------------------#
#--------------------------------End File---------------------------#
#-------------------------------------------------------------------#
def EndFile(the_file,g, idn):
    #print family records
    with open('temporaryfamilies.txt', 'r') as new_file:

        lines = new_file.readlines()
        toRemove = []
        toRemove2 = []

        for i in range(0,len(lines)):
            line = lines[i]

            if i == 0:
                if "CHIL" in line:

                    #write the unknown father in
                    the_file.write("0 @I" + str(idn+1) + "@ INDI\n" + "1 NAME Unknown//\n" +"2 GIVN Unknown\n" + "1 SEX M\n" + "1 FAMS @F001@\n")

                    #write the unknown mother in
                    the_file.write("0 @I" + str(idn+2) + "@ INDI\n" + "1 NAME Unknown//\n" +"2 GIVN Unknown\n" + "1 SEX F\n" + "1 FAMS @F001@\n")

                    #write the parents in

                    the_file.write("0 @F001@ FAM\n" + "1 HUSB @I" + str(idn+1) +'@\n' + "1 WIFE @I" + str(idn+2) +'@\n')

            else:
                pass

            #check if husb in line
            if "HUSB" in line:
                try:
                    if "WIFE" not in lines[i+1] and "CHIL" not in lines[i+1]:
                        toRemove.append(line)
                    else:
                        the_file.write(line)
                except:
                    the_file.write(line)

            #check if fam in line
            elif "FAM" in line:
                try:
                    if "HUSB" in lines[i+1] and "WIFE" not in lines[i+2] and "CHIL" not in lines[i+2]:
                        toRemove.append(line)
                    else:
                        the_file.write(line)
                except:
                    the_file.write(line)
            else:
                the_file.write(line)


    #clear temporaryfamilies.txt
    with open('temporaryfamilies.txt', 'w') as new_file:
        new_file.close

    #Print Trailer
    the_file.write('0 TRLR\n')

    #format toRemove list
    for item in toRemove:

        newItem = item.strip('\n').split()
        newItem = newItem[1]

        if "@F" in newItem:
            toRemove2.append(newItem)

    the_file.close()

    #fix family groups
    with open (g, 'r', encoding='utf-8') as read_file:
        fixFams = read_file.readlines()

    with open(g, 'w', encoding='utf-8') as in_file:
        for line in fixFams:

            if any(x in str(line) for x in toRemove2):
                pass
            else:
                in_file.write(line)
