#Imports
import csv
from easygui import *

#import custom modules
from header import *
from census1850 import *
from census1860 import *
from census1870 import *
from census1880 import *
from census1900 import *
from census1910 import *


#def startInterface ():
msg = "Enter the name for your final gedcom file. After hitting 'ok' select your census file from the file dialog."
title = "1850-1910 US Censuses to gedcom"
fieldNames = ["Name for final gedcom file", "Year of Census"]
fieldValues = []  #start with blanks for the values
fieldValues = multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
      if fieldValues[1].strip() != "1900" and fieldValues[1].strip() !='1910' and fieldValues[1].strip() !='1880' and fieldValues[1].strip() !='1870'and fieldValues[1].strip() !='1860' and fieldValues[1].strip() !='1850':
        errmsg = errmsg + ('Sorry, this application only accepts censuses between 1850 and 1910 at this time.\n\n')
    if errmsg == "": break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
print ("Reply was:", fieldValues[0], fieldValues[1])
fieldValuesgedname = str(fieldValues[0])
fieldValuesyear = str(fieldValues[1])

#checkbox gui for selecting specific things
question = "What information would you like to include?"
title = "This is your window title"
listOfOptions = ["option 1", "option 2", "option 3"]

choice = multchoicebox(question , title, listOfOptions)


#open a file dialogue
file_path = fileopenbox(msg="Select a csv", title="csv selection", default='*', filetypes='*.csv', multiple=False)


#root = tk.Tk()
#root.withdraw()

def main (g, y):

    g = str(g +'.ged')
    printHeader(g)
    if y == '1850':
        writeName1850(file_path , g)
    elif y == '1860':
        writeName1860(file_path , g)
    elif y == '1870':
        writeName1870(file_path , g)
    elif y == '1880':
        writeName1880(file_path , g)
    elif y == '1900':
        writeName1900(file_path , g)
    elif y == '1910':
        writeName1910(file_path, g)

    else:
        pass
        
        
    
main(fieldValuesgedname, fieldValuesyear)
