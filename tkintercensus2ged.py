#Imports
import csv
import tkinter as tk
import pickle

#import custom modules
from header import *
from census1850 import *
from census1860 import *
from census1870 import *
from census1880 import *
from census1900 import *
from census1910 import *

#load up that pickle
try:
    with open('config.pickle', 'rb') as handle:
        user_config = pickle.load(handle)
        print (user_config)
except:
    print("couldn't load user config")
class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.create_widgets()




    def create_widgets(self):

        #dictionary of countries
        self.dict = {'United States': ['1850', '1860', '1870', '1880','1900','1910'],
                    'England': ['1', '2', '3'],
                    'Sweden':['1','2','3']}

        #Label for the whole thing
        wholeLabel = tk.Label(self, text="Census2Ged", font = ("Lobster", 14, "bold italic"))
        wholeLabel.grid(row=0)

        #gedcom name label
        gednameLabel = tk.Label(self, text="Gedcom Name:", font = "Helvetica 10 bold")
        gednameLabel.grid(row=1, column=1, sticky ="w")
        #gedcom name selector
        self.gedNameSet = tk.Entry(self)
        self.gedNameSet.grid(row=1,column=2, sticky = "w")
        
        #label for country selector
        countryLabel = tk.Label(self, text="Country:", font = "Helvetica 10 bold")
        #render on left side of screen
        countryLabel.grid(row = 2,column=1, sticky="w")
        

        #label for year selector
        countryLabel = tk.Label(self, text="Census year:",font = "Helvetica 10 bold")
        #render on left side of screen
        countryLabel.grid(row = 3, column=1, sticky="w")

        #label for Tag Inclusion
        includeTagLabel = tk.Label(self, text="Tags to include",font = "Helvetica 10 bold underline")
        #render on left side of screen
        includeTagLabel.grid(row = 4, sticky="w")


        #country selector
        self.countrySelect = tk.StringVar(self)
        #year selector
        self.yearSelect = tk.StringVar(self)
        #checkbox Immigration
        self.optionImmigration = tk.IntVar(self)
        #checkbox Occupation
        self.optionOccupation = tk.IntVar(self)
        #checkbox Race
        self.optionRace = tk.IntVar(self)
        #checkbox literacy
        self.optionLiteracy=tk.IntVar(self)
        #checkbox Disability
        self.optionDisability=tk.IntVar(self)
        #checkbox Children Born
        self.optionChildrenBorn=tk.IntVar(self)
        #checkbox Military
        self.optionMilitary=tk.IntVar(self)
        #checkbox Property
        self.optionProperty=tk.IntVar(self)
        #checkbox Language
        self.optionLanguage=tk.IntVar(self)


        #update year select based on country select
        self.countrySelect.trace('w', self.update_options)
        
        #update country variable
        self.countrySelect.trace('w', self.__update_country__)
        

        #update year variable
        self.yearSelect.trace('w', self.__update_year__)

        #update Immigration variable
        self.optionImmigration.trace('w', self.__update_immigration__)

        #update Occupation variable
        self.optionOccupation.trace('w', self.__update_occupation__)
        
        #update Race variable
        self.optionRace.trace('w', self.__update_race__)

        #update Literacy variable
        self.optionLiteracy.trace('w', self.__update_literacy__)

        #update disability variable
        self.optionDisability.trace('w', self.__update_disability__)

        #update children variable
        self.optionChildrenBorn.trace('w', self.__update_children__)

        #update Military variable
        self.optionMilitary.trace('w', self.__update_military__)

        #update Property variable
        self.optionProperty.trace('w', self.__update_property__)

        #update Language variable
        self.optionLanguage.trace('w', self.__update_language__)

        #render the country options menu
        self.countryOptions = tk.OptionMenu(self, self.countrySelect, *self.dict.keys())
        self.yearOptions = tk.OptionMenu(self, self.yearSelect, '')


        #set United States as the default value
        self.countrySelect.set("United States")



        #render on right side of widget
        self.countryOptions.grid(row = 2, column = 2, sticky="w")
        self.yearOptions.grid(row=3,column=2, sticky="w")

        # #renders a separation line between widgets
        #separator = tk.Frame(height=2, bd=1, relief= tk.SUNKEN)
        #separator.pack(fill= tk.X, padx=5, pady=5)

        #checkbutton widgets

        #Immigration
        self.CheckboxImmigration = tk.Checkbutton(self, text="Immigration Year", variable=self.optionImmigration)
        self.CheckboxImmigration.grid(row=5, sticky="w")

        #Immigration tag entry box
        self.immigrationSet = tk.Entry(self)
        self.immigrationSet.grid(row=5,column=1, sticky = "w")
        
        #Occupation
        self.CheckboxOccupation = tk.Checkbutton(self, text="Occupation", variable=self.optionOccupation)
        self.CheckboxOccupation.grid(row=5,column=2, sticky="w")

        #Occupation tag entry box
        self.occupationSet = tk.Entry(self)
        self.occupationSet.grid(row=5,column=3, sticky = "w")

        #Race
        self.CheckboxRace = tk.Checkbutton(self,text="Race", variable=self.optionRace)
        self.CheckboxRace.grid(row=6, sticky="w")

        #Race tag entry box
        self.raceSet = tk.Entry(self)
        self.raceSet.grid(row=6,column=1, sticky = "w")

        #Literacy
        self.CheckboxLiteracy = tk.Checkbutton(self, text = "Literacy", variable=self.optionLiteracy)
        self.CheckboxLiteracy.grid(row=6, column = 2, sticky = "w")
        
        #Literacy tag entry box
        self.literacySet = tk.Entry(self)
        self.literacySet.grid(row=6,column=3, sticky = "w")


        #Disability
        self.CheckboxDisability = tk.Checkbutton(self, text = "Disability", variable = self.optionDisability)
        self.CheckboxDisability.grid(row = 7, sticky = "w")

        #Disability tag entry box
        self.disabilitySet = tk.Entry(self)
        self.disabilitySet.grid(row=7,column=1, sticky = "w")

        #Children Born
        self.CheckboxChildrenBorn = tk.Checkbutton(self, text="Children Born", variable = self.optionChildrenBorn)
        self.CheckboxChildrenBorn.grid(row=7, column=2, sticky="w")

        #Children Born tag entry box
        self.childrenBornSet = tk.Entry(self)
        self.childrenBornSet.grid(row=7,column=3, sticky = "w")

        #Military
        self.CheckboxMilitary = tk.Checkbutton(self, text="Military", variable=self.optionMilitary)
        self.CheckboxMilitary.grid(row=8,sticky="w")

        #Property
        self.CheckboxProperty = tk.Checkbutton(self, text = "Property", variable=self.optionProperty)
        self.CheckboxProperty.grid(row=8,column=1,sticky="w")

        #Language
        self.CheckboxLanguage = tk.Checkbutton(self,text="Language", variable=self.optionLanguage)
        self.CheckboxLanguage.grid(row=9,sticky="w")

        #CSV file select label
        self.PathLabel = tk.Label(self)
        self.PathLabel.grid(row=10,column=1, sticky="w")

        #CSV file select button
        self.BrowseButton = tk.Button(self, text="Input CSV",font = "Helvetica 10 bold", command=self.browse_func)
        self.BrowseButton.grid(row=10, sticky ="w")

        #submit button
        self.submit = tk.Button(self, text="Submit",
                                command = self.__Submit_Button__)
        #,Literacy,Disability,Children,Military,Property,Language
        self.submit.grid(row=11,column=1, sticky="w")
        #Quit button
        self.quit = tk.Button(self, text="QUIT", fg="red",
                             command= self.quit_sequence)
        self.quit.grid(row =11, column =2,sticky="w")

        #set up previous user configurations
        try:
            if user_config["Race"] == 1:
                self.CheckboxRace.select()
            if user_config["Military"] == 1:
                self.CheckboxMilitary.select()
            if user_config["Literacy"] == 1:
                self.CheckboxLiteracy.select()
            if user_config["Immigration"] == 1:
                self.CheckboxImmigration.select()
            if user_config["Disability"] == 1:
                self.CheckboxDisability.select()
            if user_config["Children Born"] == 1:
                self.CheckboxChildrenBorn.select()
            if user_config["Occupation"] == 1:
                self.CheckboxOccupation.select()
            if user_config["Property"] == 1:
                self.CheckboxProperty.select()
            if user_config["Language"] == 1:
                self.CheckboxLanguage.select()

        except:
            print("nope")

    

    #quit
    def quit_sequence(self, *args):
        root.destroy()

#var.get() ---checked / 1
#not var.get() ---not checked / 0
    def browse_func(self):
        filename = tk.filedialog.askopenfilename()
        self.PathLabel.config(text=filename)
        return (filename)

    #update options list of years
    def update_options(self, *args):
        countries = self.dict[self.countrySelect.get()]
        self.yearSelect.set(countries[0])

        menu = self.yearOptions['menu']
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.yearSelect.set(nation))

    def __update_country__(self, *args):
        Country = self.countrySelect.get()
        print (Country)
        return(Country)
    
    def __update_year__(self, *args):
        Year = self.yearSelect.get()
        print (Year)
        return(Year)

    def __update_immigration__(self, *args):
        Immigration = self.optionImmigration.get()
        print (Immigration)
        return(Immigration)

    def __update_occupation__(self, *args):
        Occupation = self.optionOccupation.get()
        print (Occupation)
        return(Occupation)

    def __update_race__(self, *args):
        Race = self.optionRace.get()
        print (Race)
        return(Race)

    def __update_literacy__(self, *args):
        Literacy = self.optionLiteracy.get()
        print (Literacy)
        return(Literacy)

    def __update_disability__(self, *args):
        Disability = self.optionDisability.get()
        print (Disability)
        return(Disability)

    def __update_children__(self, *args):
        Children = self.optionChildrenBorn.get()
        print (Children)
        return(Children)

    def __update_military__(self, *args):
        Military = self.optionMilitary.get()
        print (Military)
        return(Military)

    def __update_property__(self, *args):
        Property = self.optionProperty.get()
        print (Property)
        return(Property)

    def __update_language__(self, *args):
        Language = self.optionLanguage.get()
        print (Language)
        return(Language)

    # create configDictionary with all the values of the fields
    def __Update_Checkbox_List__(self):
        variable_list ={"Country" : self.countrySelect.get() , 
                        "Year" : self.yearSelect.get(),
                        "Immigration" : self.optionImmigration.get(),
                        "Occupation" : self.optionOccupation.get(),
                        "Race" : self.optionRace.get(),
                        "Literacy" : self.optionLiteracy.get(),
                        "Disability" : self.optionDisability.get(),
                        "Children Born" : self.optionChildrenBorn.get(),
                        "Military" : self.optionMilitary.get(),
                        "Gedname" : self.gedNameSet.get(),
                        "Property" : self.optionProperty.get(),
                        "Language" : self.optionLanguage.get()
                        }

        print(variable_list)
        return (variable_list)

    def __Submit_Button__(self):
        variable_list = self.__Update_Checkbox_List__()
        
        #save the current file configuration
        with open ("config.pickle", 'wb') as config_file:
            pickle.dump(variable_list, config_file, protocol=pickle.HIGHEST_PROTOCOL)
        
        #run the main function
        self.main(variable_list)


    #based on the name of the gedcom file and year
    def main (self, configDictionary):
        g = configDictionary["Gedname"]
        y = configDictionary["Year"]

        g = str(g +'.ged')

        file_path = self.PathLabel.cget("text")
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
            writeName1910(file_path, g, configDictionary)

        else:
            pass
           



#Run the Gui
root = tk.Tk()
root.minsize(225, 225)

#background color
app = Application(master=root)


app.mainloop()

    
