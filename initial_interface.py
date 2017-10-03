#Imports
from easygui import *

#initial_interface custom module. Asks for name of output file. 
def startInterface ():
    msg = "Enter the name for your final gedcom file. After hitting 'ok' select your census file from the file dialog."
    title = "1900 Census to gedcom"
    fieldNames = ["Name for final gedcom file"]
    fieldValues = []  #start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)

    # make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
          if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    print ("Reply was:", fieldValues)
    fieldValues2 = str(fieldValues)
    fieldValues2 = fieldValues2[2:-2]
    return fieldValues2
